# Copyright 2026 Gerard Ando
# SPDX-License-Identifier: MPL-2.0
from dataclasses import replace
import unittest

from therma_commons import verification as v


class VerificationTests(unittest.TestCase):
    def test_readiness_drops_and_fault_reset_cannot_restore_dwell(self):
        good = v.IntervalEvidence()
        ready = v.advance(v.Readiness(dwell_intervals=59), good)
        self.assertTrue(ready.verified)
        self.assertEqual(v.advance(ready, replace(good, in_band=False)), v.Readiness())

        bad = replace(good, fresh=False)
        fault = v.advance(ready, bad)
        self.assertEqual(fault, v.Readiness(fault_latched=True))
        self.assertEqual(v.advance(fault, bad, manual_reset=True), fault)
        self.assertEqual(v.advance(fault, good), fault)
        self.assertEqual(v.advance(fault, good, manual_reset=True), v.Readiness())
        self.assertFalse(v.advance(v.Readiness(), good).verified)

    def test_finite_state_space(self):
        result = v.verify_readiness()
        self.assertEqual(result["transitions"], 31_744)
        self.assertTrue(result["all_properties_hold"])

    def test_thermal_budget_respects_reference_limits(self):
        self.assertAlmostEqual(v.USEFUL_J, 41_840)
        self.assertGreater(v.TRANSPORTED_J, v.USEFUL_J)
        self.assertLess(v.thermal_case(160, 1.8)["cool_cop_over_carnot"], 1)
        with self.assertRaises(ValueError):
            v.thermal_case(160, v.CARNOT_COP + .1)

    def test_percentiles_and_sensitivity(self):
        result = v.simulate(20261123, 1000)
        self.assertEqual(set(result["regimes"]), set(v.REGIMES))
        for regime in result["regimes"].values():
            for metric in regime["quantiles"].values():
                self.assertLessEqual(metric["p01"], metric["p50"])
                self.assertLessEqual(metric["p50"], metric["p99"])
            self.assertAlmostEqual(sum(regime["sensitivity"]["rnpv_variance_shares"].values()), 1)


if __name__ == "__main__":
    unittest.main()
