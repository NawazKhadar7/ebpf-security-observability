import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
class MetricTests(unittest.TestCase):
    def test_oracle_detects_error(self):
        with self.assertRaises(AssertionError): check({'metrics':{'count':3}}, {'checks':{'count':{'equals':4}}})
    def test_oracle_bounds(self):
        self.assertTrue(check({'metrics':{'count':4}}, {'checks':{'count':{'min':1,'max':5}}}))
        with self.assertRaises(AssertionError): check({'metrics':{}},{'checks':{'count':{'min':0}}})
