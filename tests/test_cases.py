import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
class WorkloadTests(unittest.TestCase):
    def test_all_independent_oracles(self):
        self.assertEqual(len(cases()),36)
        for path in cases():
            with self.subTest(case=path.name): evaluate(path)
    def test_unique_cases_and_seeds(self):
        values=[json.loads(p.read_text()) for p in cases()]
        self.assertEqual(len({v['id'] for v in values}),36)
        self.assertEqual(len({v['family'] for v in values}),6)
