import copy
import math
import unittest
from therma_commons.control import Config, Controller, Reading, State
from therma_commons.simulation import simulate
from therma_commons.analysis import analyze_trial, wilson_interval


class ControlTests(unittest.TestCase):
    def test_transitions_and_mutual_exclusion(self):
        for temp, expected in [(20,State.HEAT),(60,State.COOL),(40,State.VERIFY)]:
            command=Controller(Config()).step(Reading(0,temp),0)
            self.assertEqual(command.state,expected)
            self.assertEqual(command.heat_fraction*command.cool_fraction,0)

    def test_dwell_resets_after_excursion(self):
        c=Controller(Config(dwell_s=2))
        for t,temp in [(0,40),(1,42),(2,40),(3,40)]:
            self.assertNotEqual(c.step(Reading(t,temp),t).state,State.READY)
        self.assertEqual(c.step(Reading(4,40),4).state,State.READY)

    def test_faults_latch_with_no_actuation(self):
        readings=[Reading(0,float('nan')),Reading(0,80),Reading(-5,40),
                  Reading(0,40,False),Reading(0,40,True,False),Reading(1,40)]
        for reading in readings:
            with self.subTest(reading=reading):
                c=Controller(Config())
                self.assertEqual(c.step(reading,0).state,State.FAULT)
                cmd=c.step(Reading(2,20),2)
                self.assertEqual((cmd.state,cmd.heat_fraction,cmd.cool_fraction),(State.FAULT,0,0))

    def test_duplicate_clock_and_sample_rejected(self):
        for sample,now in [(Reading(0,20),1),(Reading(1,20),0)]:
            c=Controller(Config());c.step(Reading(0,20),0)
            self.assertEqual(c.step(sample,now).state,State.FAULT)

    def test_timeout(self):
        c=Controller(Config(timeout_s=3,dwell_s=1))
        c.step(Reading(0,20),0)
        self.assertEqual(c.step(Reading(3,20),3).state,State.FAULT)

    def test_bad_config(self):
        for kw in [{'target_c':90},{'dwell_s':0},{'gain_per_c':math.inf}, {'minimum_c':30}]:
            with self.assertRaises(ValueError): Config(**kw)


class SimulationTests(unittest.TestCase):
    def test_declared_matrix_converges(self):
        for mass in [250,500,750]:
            for start,target in [(20,40),(20,60),(60,40),(40,20)]:
                r=simulate(mass,start,target)
                self.assertEqual(r['status'],'ready')
                self.assertIn('SYNTHETIC',r['provenance'])
                self.assertGreater(r['samples'][-1]['wall_energy_wh'],0)
                self.assertTrue(all(s['heat_fraction']*s['cool_fraction']==0 for s in r['samples']))

    def test_invalid_mass(self):
        with self.assertRaises(ValueError):simulate(0)


class AnalysisTests(unittest.TestCase):
    def fixture(self):
        return {'provenance':'measured','trial_id':'unit-test-only','target_c':40,
                'expanded_uncertainty_c':0.2,'completion_s':60,
                'reference_sensor_ids':['a','b','c'],
                'samples':[{'timestamp_s':t,'reference_c':[40,40.1,39.9]} for t in range(61)]}

    def test_pass_and_uncertainty_failure(self):
        d=self.fixture();self.assertTrue(analyze_trial(d)['passed'])
        d['expanded_uncertainty_c']=1
        self.assertFalse(analyze_trial(d)['passed'])

    def test_one_bad_reference_fails(self):
        d=self.fixture();d['samples'][25]['reference_c'][0]=42
        self.assertFalse(analyze_trial(d)['passed'])

    def test_incomplete_nonfinite_and_synthetic_rejected(self):
        for change in ['gap','nan','synthetic','duplicate','reference']:
            d=self.fixture()
            if change=='gap': del d['samples'][30]
            if change=='nan': d['samples'][0]['reference_c'][0]=float('nan')
            if change=='synthetic': d['provenance']='synthetic'
            if change=='duplicate':d['samples'][1]['timestamp_s']=0
            if change=='reference':d['reference_sensor_ids']=['a','a','a']
            with self.assertRaises(ValueError):analyze_trial(d)

    def test_timeout_and_confidence_interval(self):
        d=self.fixture();d['completion_s']=1800
        for s in d['samples']:s['timestamp_s']+=1740
        self.assertFalse(analyze_trial(d)['passed'])
        lo,hi=wilson_interval(57,60)
        self.assertLess(lo,.95);self.assertGreater(hi,.95)


if __name__=='__main__': unittest.main()
