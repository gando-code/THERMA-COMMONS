# Copyright 2026 Gerard Ando
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Offline independent reference analysis; rejects incomplete/misleading records."""
import math


def analyze_trial(data):
    """Analyze normalized reference data for one protocol-v1 trial.

    Pass requires 61 samples at <=1 s intervals spanning the full 60 s
    window ending at declared completion, three independent reference channels,
    <=30 minute cycle time and uncertainty-guarded +/-1 C error throughout.
    This function does not establish calibration validity or food safety.
    """
    def finite(v):
        return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)
    if data.get("provenance") != "measured":
        raise ValueError("only explicitly measured records qualify for validation")
    target = data.get("target_c")
    uncertainty = data.get("expanded_uncertainty_c")
    completion = data.get("completion_s")
    if not all(finite(x) for x in (target, uncertainty, completion)):
        raise ValueError("finite target, uncertainty and completion required")
    if not 20 <= target <= 60 or uncertainty < 0 or completion < 60:
        raise ValueError("invalid endpoint metadata")
    refs = data.get("reference_sensor_ids", [])
    if len(refs) != 3 or len(set(refs)) != 3 or not all(isinstance(x,str) and x for x in refs):
        raise ValueError("three distinct independent reference sensor IDs required")
    samples = data.get("samples", [])
    last = None
    for s in samples:
        t = s.get("timestamp_s")
        values = s.get("reference_c", [])
        if not finite(t) or t < 0 or (last is not None and t <= last):
            raise ValueError("sample times must be finite, nonnegative and increasing")
        if len(values) != 3 or not all(finite(x) for x in values):
            raise ValueError("each sample needs three finite reference values")
        last = t
    window = [s for s in samples if completion-60 <= s["timestamp_s"] <= completion]
    if len(window) < 61:
        raise ValueError("incomplete verification window")
    if window[0]["timestamp_s"] != completion-60 or window[-1]["timestamp_s"] != completion:
        raise ValueError("verification window endpoints missing")
    if any(b["timestamp_s"]-a["timestamp_s"] > 1 for a,b in zip(window,window[1:])):
        raise ValueError("reference sampling gap exceeds one second")
    worst = max(abs(v-target)+uncertainty for s in window for v in s["reference_c"])
    gradient = max(max(s["reference_c"])-min(s["reference_c"]) for s in window)
    passed = worst <= 1 and gradient <= 2 and completion < 1800
    return {"trial_id": data.get("trial_id"), "passed": passed,
            "max_guard_banded_error_c": worst, "max_spatial_range_c": gradient,
            "window_samples": len(window), "completion_s": completion,
            "qualification": "defined thermal endpoint only; no food-safety inference"}


def wilson_interval(passed, total):
    if total <= 0 or not 0 <= passed <= total:
        raise ValueError("invalid counts")
    z = 1.959963984540054
    p = passed / total
    denominator = 1 + z*z/total
    center = (p + z*z/(2*total))/denominator
    radius = z * math.sqrt(p*(1-p)/total + z*z/(4*total*total))/denominator
    return [max(0,center-radius), min(1,center+radius)]
