# Copyright 2026 Gerard Ando
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Deterministic research state machine. Outputs are simulated requests, not IO."""
from dataclasses import dataclass
from enum import Enum
import math


class State(str, Enum):
    IDLE = "idle"
    HEAT = "heat"
    COOL = "cool"
    VERIFY = "verify"
    READY = "ready"
    FAULT = "fault"


@dataclass(frozen=True)
class Reading:
    timestamp_s: float
    temperature_c: float
    load_present: bool = True
    mixer_ok: bool = True


@dataclass(frozen=True)
class Command:
    state: State
    heat_fraction: float = 0.0
    cool_fraction: float = 0.0
    reason: str = ""


@dataclass(frozen=True)
class Config:
    target_c: float = 40.0
    tolerance_c: float = 0.5
    dwell_s: float = 60.0
    timeout_s: float = 1800.0
    stale_s: float = 2.0
    maximum_c: float = 75.0
    minimum_c: float = 0.0
    gain_per_c: float = 0.2

    def __post_init__(self):
        values = vars(self).values()
        if not all(math.isfinite(v) for v in values):
            raise ValueError("configuration must be finite")
        if not 20 <= self.target_c <= 60:
            raise ValueError("prototype targets must be 20 through 60 C")
        if not self.minimum_c < 20 or not self.maximum_c > 60:
            raise ValueError("limits must bracket the full target range")
        if any(v <= 0 for v in (self.tolerance_c, self.dwell_s,
                               self.timeout_s, self.stale_s, self.gain_per_c)):
            raise ValueError("timing, tolerance and gain must be positive")
        if self.dwell_s >= self.timeout_s:
            raise ValueError("dwell must be shorter than timeout")


class Controller:
    """Single-channel control logic; READY is not independent verification.

    Faults and completion latch. Construct a new instance for a fresh run.
    An external independent logger must establish actual endpoint performance.
    """

    def __init__(self, config: Config):
        self.config = config
        self.state = State.IDLE
        self.started = None
        self.last_now = None
        self.last_sample = None
        self.in_band_since = None
        self.reason = ""

    def _fault(self, reason):
        self.state = State.FAULT
        self.reason = reason
        return Command(self.state, reason=reason)

    def step(self, reading: Reading, now_s: float) -> Command:
        if self.state in (State.FAULT, State.READY):
            return Command(self.state, reason=self.reason)
        c = self.config
        if not all(math.isfinite(v) for v in
                   (now_s, reading.timestamp_s, reading.temperature_c)):
            return self._fault("nonfinite measurement or time")
        if self.last_now is not None and now_s <= self.last_now:
            return self._fault("nonmonotonic controller clock")
        self.last_now = now_s
        if reading.timestamp_s > now_s or now_s - reading.timestamp_s > c.stale_s:
            return self._fault("stale or future measurement")
        if self.last_sample is not None and reading.timestamp_s <= self.last_sample:
            return self._fault("measurement did not advance")
        self.last_sample = reading.timestamp_s
        if not reading.load_present:
            return self._fault("load missing")
        if not reading.mixer_ok:
            return self._fault("mixing unavailable")
        if not c.minimum_c < reading.temperature_c < c.maximum_c:
            return self._fault("measurement outside protective limits")
        if self.started is None:
            self.started = now_s
        if now_s - self.started >= c.timeout_s:
            return self._fault("cycle timeout")
        error = c.target_c - reading.temperature_c
        if abs(error) <= c.tolerance_c:
            if self.in_band_since is None:
                self.in_band_since = now_s
            if now_s - self.in_band_since >= c.dwell_s:
                self.state = State.READY
                self.reason = "control-channel dwell complete; reference review required"
            else:
                self.state = State.VERIFY
            if self.state == State.READY:
                return Command(self.state, reason=self.reason)
            # Continue low-power correction during dwell; switching all power
            # off at the band edge can repeatedly lose the endpoint to ambient.
            fraction = min(1.0, abs(error) * c.gain_per_c)
            return Command(self.state,
                           heat_fraction=fraction if error > 0 else 0.0,
                           cool_fraction=fraction if error < 0 else 0.0)
        self.in_band_since = None
        power = min(1.0, abs(error) * c.gain_per_c)
        if error > 0:
            self.state = State.HEAT
            return Command(self.state, heat_fraction=power)
        self.state = State.COOL
        return Command(self.state, cool_fraction=power)
