import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
class RegressionTests(unittest.TestCase):
    def test_example_matches_real_run(self):
        case=json.loads((ROOT/'examples/request.json').read_text())
        expected=json.loads((ROOT/'examples/response.json').read_text())
        self.assertEqual(run_case(case)['metrics'],expected['metrics'])
    def test_expected_files_are_independent_specifications(self):
        for path in cases():
            oracle=json.loads(path.with_name(path.name.replace('.case.json','.expected.json')).read_text())
            self.assertGreater(len(oracle['checks']),1); self.assertTrue(oracle['rationale'])
