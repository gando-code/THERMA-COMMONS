# Copyright 2026 Gerard Ando
# SPDX-License-Identifier: MPL-2.0
"""Offline, synthetic thermodynamic, readiness-logic and economic verification."""

import argparse
from dataclasses import asdict, dataclass, replace
from itertools import product
import json
import math
from pathlib import Path
import random
import statistics


# All uncertain ranges are uniform sensitivity inputs, not calibrated priors.
@dataclass(frozen=True)
class Regime:
    annual_units: tuple
    margin_usd: tuple
    program_cost_usd: tuple
    probabilities: tuple
    cooling_w: tuple
    cooling_cop: tuple


REGIMES = {
    "alpha": Regime((200, 1800), (100, 500), (100_000, 150_000),
                    (.70, .85, .65), (90, 230), (.8, 2.8)),
    "beta": Regime((60, 700), (100, 420), (145_000, 245_000),
                   (.60, .65, .55), (45, 175), (.65, 2.15)),
    "gamma": Regime((40, 550), (40, 300), (100_000, 210_000),
                    (.55, .80, .50), (25, 155), (.5, 1.9)),
    "delta": Regime((100, 1100), (60, 380), (110_000, 170_000),
                    (.55, .80, .50), (60, 200), (.7, 2.5)),
}
DISCOUNT_RATE = .15
YEARS = 3
ANNUITY = sum((1 + DISCOUNT_RATE) ** -year for year in range(1, YEARS + 1))
WATER_CP = 4184.0  # J/(kg K), rounded engineering approximation
LOAD_KG = .5
CHANGE_K = 20.0
USEFUL_J = LOAD_KG * WATER_CP * CHANGE_K
COUPLED_CAPACITANCE_J_PER_K = 250.0
TRANSPORTED_J = USEFUL_J + COUPLED_CAPACITANCE_J_PER_K * CHANGE_K
EVAPORATOR_K = 283.15
CONDENSER_K = 328.15
CARNOT_COP = EVAPORATOR_K / (CONDENSER_K - EVAPORATOR_K)
AUXILIARY_W = 20.0
HEATER_W = 300.0
HEAT_TRANSFER_FRACTION = .85
HEATING_LOSS_W = 15.0
DWELL_S = 60.0


@dataclass(frozen=True)
class IntervalEvidence:
    # In this abstraction probes agree within the declared uncertainty budget.
    fresh: bool = True
    in_band: bool = True
    probe_agreement: bool = True
    mixer_ok: bool = True
    vessel_ok: bool = True
    safety_ok: bool = True
    image_attested: bool = True
    controller_alive: bool = True

    @property
    def permissive(self):
        return all(vars(self).values())


@dataclass(frozen=True)
class Readiness:
    # These are research outputs. No commands drive energized hardware.
    fault_latched: bool = False
    dwell_intervals: int = 0
    verified: bool = False


def advance(state, evidence, manual_reset=False, required_intervals=60):
    if not all((evidence.fresh, evidence.probe_agreement, evidence.mixer_ok,
                evidence.vessel_ok, evidence.safety_ok, evidence.image_attested,
                evidence.controller_alive)):
        return Readiness(fault_latched=True)
    if state.fault_latched:
        return Readiness(fault_latched=not manual_reset)
    if not evidence.in_band:
        return Readiness()
    intervals = min(required_intervals, state.dwell_intervals + 1)
    return Readiness(dwell_intervals=intervals, verified=intervals == required_intervals)


def verify_readiness(required_intervals=60):
    """Exhaust the reachable finite-state model at the declared sample tick."""
    if required_intervals < 1:
        raise ValueError("require a positive dwell")
    evidence_space = [IntervalEvidence(*values) for values in product((False, True), repeat=8)]
    states = [Readiness(dwell_intervals=i, verified=i == required_intervals)
              for i in range(required_intervals + 1)]
    states.append(Readiness(fault_latched=True))
    reachable = {Readiness()}
    cases = 0
    for state, evidence, reset in product(states, evidence_space, (False, True)):
        result = advance(state, evidence, reset, required_intervals)
        properties = (
            not result.verified or (evidence.permissive and not state.fault_latched
                                    and state.dwell_intervals >= required_intervals - 1),
            not result.fault_latched or (not result.verified and result.dwell_intervals == 0),
            not state.fault_latched or reset or result.fault_latched,
            evidence.permissive or not result.verified,
            result in states,
        )
        if not all(properties):
            raise RuntimeError(f"readiness invariant violation: {state}, {evidence}, {reset}")
        cases += 1
    # Reach every listed state from the initial condition with concrete witnesses.
    state = Readiness()
    for _ in range(required_intervals):
        state = advance(state, IntervalEvidence(), required_intervals=required_intervals)
        reachable.add(state)
    reachable.add(advance(state, replace(IntervalEvidence(), safety_ok=False),
                          required_intervals=required_intervals))
    if reachable != set(states):
        raise RuntimeError("state enumeration and reachable witnesses disagree")
    return {"states": len(states), "transitions": cases, "sample_tick_s": 1,
            "dwell_intervals": required_intervals, "all_properties_hold": True}


def thermal_case(cooling_w, cooling_cop):
    if not (cooling_w > 0 and 0 < cooling_cop <= CARNOT_COP):
        raise ValueError("cooling assumptions must stay inside the modeled envelope")
    heating_time = TRANSPORTED_J / (HEATER_W * HEAT_TRANSFER_FRACTION - HEATING_LOSS_W)
    cooling_time = TRANSPORTED_J / cooling_w
    # Gross heat extracted equals net useful-path extraction in this simple model.
    # Unmeasured parasitic heat loads make this electrical budget optimistic.
    cooling_j = TRANSPORTED_J / cooling_cop + AUXILIARY_W * (cooling_time + DWELL_S)
    heating_j = HEATER_W * heating_time + AUXILIARY_W * (heating_time + DWELL_S)
    return {
        "cool_ready_s": cooling_time + DWELL_S,
        "heat_ready_s": heating_time + DWELL_S,
        "cool_cop_over_carnot": cooling_cop / CARNOT_COP,
        "wall_energy_wh": (cooling_j + heating_j) / 3600,
        "wall_thermal_service_yield": 2 * USEFUL_J / (cooling_j + heating_j),
    }


def program_value(units, margin, cost, regime):
    conditional_pv = units * margin * ANNUITY
    expected_pv = conditional_pv * math.prod(regime.probabilities)
    return {"rnpv_usd": expected_pv - cost, "roi": (expected_pv - cost) / cost}


def percentiles(values):
    values = sorted(values)
    result = {}
    for name, quantile in (("p01", .01), ("p50", .50), ("p99", .99)):
        index = quantile * (len(values) - 1)
        lower = math.floor(index)
        result[name] = values[lower] + (values[math.ceil(index)] - values[lower]) * (index - lower)
    return result


def sensitivity(regime):
    """Exact first-order Sobol indices for independent Uniform inputs and rNPV."""
    def variance(bounds):
        return (bounds[1] - bounds[0]) ** 2 / 12

    units_mu, margin_mu, cost_mu = map(statistics.mean,
                                       (regime.annual_units, regime.margin_usd, regime.program_cost_usd))
    units_var, margin_var, cost_var = map(variance,
                                         (regime.annual_units, regime.margin_usd, regime.program_cost_usd))
    k_squared = (ANNUITY * math.prod(regime.probabilities)) ** 2
    parts = {
        "annual_units": k_squared * units_var * margin_mu ** 2,
        "unit_margin": k_squared * margin_var * units_mu ** 2,
        "program_cost": cost_var,
        "units_margin_interaction": k_squared * units_var * margin_var,
    }
    total = sum(parts.values())
    cases = {name: program_value(units_mu * scale, margin_mu, cost_mu, regime)["roi"]
             for name, scale in (("minus_20pct", .8), ("base", 1), ("plus_20pct", 1.2))}
    return {"rnpv_variance_usd_squared": total,
            "rnpv_variance_shares": {key: value / total for key, value in parts.items()},
            "roi_at_unit_volume_swings": cases}


def simulate(seed, draws):
    if draws < 1000:
        raise ValueError("at least 1000 draws are needed for tail reporting")
    rng = random.Random(seed)
    results = {}
    for name, regime in REGIMES.items():
        metrics = {}
        for _ in range(draws):
            units = rng.uniform(*regime.annual_units)
            margin = rng.uniform(*regime.margin_usd)
            cost = rng.uniform(*regime.program_cost_usd)
            power = rng.uniform(*regime.cooling_w)
            cop = rng.uniform(*regime.cooling_cop)
            values = program_value(units, margin, cost, regime) | thermal_case(power, cop)
            for metric, value in values.items():
                metrics.setdefault(metric, []).append(value)
        results[name] = {"inputs": asdict(regime), "quantiles": {
            metric: percentiles(values) for metric, values in metrics.items()
        }, "sensitivity": sensitivity(regime)}
    return {
        "classification": "synthetic feasibility sensitivity; no measured or certified performance",
        "seed": seed,
        "draws_per_regime": draws,
        "readiness_logic": verify_readiness(),
        "constants": {"water_cp_j_per_kg_k": WATER_CP, "useful_j_per_direction": USEFUL_J,
                      "transported_j_per_direction": TRANSPORTED_J, "carnot_cop": CARNOT_COP,
                      "annuity": ANNUITY, "years": YEARS, "discount_rate": DISCOUNT_RATE,
                      "evaporator_k": EVAPORATOR_K, "condenser_k": CONDENSER_K,
                      "heat_transfer_fraction": HEAT_TRANSFER_FRACTION,
                      "heater_w": HEATER_W, "heating_loss_w": HEATING_LOSS_W,
                      "coupled_capacitance_j_per_k": COUPLED_CAPACITANCE_J_PER_K,
                      "load_kg": LOAD_KG, "change_k": CHANGE_K, "dwell_s": DWELL_S,
                      "auxiliary_w": AUXILIARY_W},
        "regimes": results,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20261123)
    parser.add_argument("--draws", type=int, default=20_000)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        report = simulate(args.seed, args.draws)
    except ValueError as exc:
        parser.error(str(exc))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, allow_nan=False, indent=2) + "\n", encoding="utf-8")
    print(f"Synthetic verification written to {args.output}")


if __name__ == "__main__":
    main()
