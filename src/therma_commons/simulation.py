# Copyright 2026 Gerard Ando
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Idealized well-mixed lumped thermal model; not a food or hardware digital twin."""
import math
from .control import Config, Controller, Reading, State


def simulate(mass_g=500.0, start_c=20.0, target_c=40.0):
    if not all(math.isfinite(x) for x in (mass_g, start_c, target_c)):
        raise ValueError("inputs must be finite")
    if mass_g not in (250, 500, 750):
        raise ValueError("supported experimental masses are 250, 500 and 750 g")
    if not 0 < start_c < 75:
        raise ValueError("starting temperature outside simulation envelope")
    controller = Controller(Config(target_c=target_c))
    temperature = start_c
    energy_j = 0.0
    samples = []
    # Constant assumptions: water cp 4180 J/kg/K, 500 W heat delivered,
    # 200 W net cooling at full output, 600/150 W electrical input,
    # 0.5 W/K ambient conductance, 5 W auxiliary power. No measured fitting.
    for second in range(1801):
        cmd = controller.step(Reading(float(second), temperature), float(second))
        samples.append({"timestamp_s": second, "control_c": temperature,
                        "state": cmd.state.value, "heat_fraction": cmd.heat_fraction,
                        "cool_fraction": cmd.cool_fraction,
                        "wall_energy_wh": energy_j / 3600.0})
        if cmd.state in (State.READY, State.FAULT):
            return {"provenance": "SYNTHETIC SIMULATION - NOT EXPERIMENTAL EVIDENCE",
                    "model": "well-mixed water; fixed assumed heat rates",
                    "mass_g": mass_g, "start_c": start_c, "target_c": target_c,
                    "status": cmd.state.value, "reason": cmd.reason,
                    "elapsed_s": second, "samples": samples}
        q = 500 * cmd.heat_fraction - 200 * cmd.cool_fraction - 0.5 * (temperature - 20)
        temperature += q / (mass_g / 1000 * 4180)
        energy_j += 600 * cmd.heat_fraction + 150 * cmd.cool_fraction + 5
    raise RuntimeError("simulation failed to terminate")
