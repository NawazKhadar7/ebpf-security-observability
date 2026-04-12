import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
class ValidationTests(unittest.TestCase):
    def test_reject_bad_inputs(self):
        for case in ({},[],{'id':'x','family':'x','size':0,'seed':0},{'id':'x','family':'x','size':True,'seed':0}):
            with self.subTest(case=case),self.assertRaises(ValueError): validate_case(case)
    def test_reject_unknown_family(self):
        with self.assertRaises(ValueError): run_case({'id':'bad','family':'not-a-family','size':4,'seed':1})
