import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
class BoundaryTests(unittest.TestCase):
    def test_finite_values(self):
        for value in (float('inf'),float('nan'),'3'):
            with self.subTest(value=value),self.assertRaises(ValueError): finite_numbers([value])
    def test_case_range_boundaries(self):
        self.assertEqual(validate_case({'id':'x','family':'x','size':1,'seed':0})['size'],1)
        for size in (-1,10001):
            with self.assertRaises(ValueError): validate_case({'id':'x','family':'x','size':size,'seed':0})
