import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
class CoreTests(unittest.TestCase):
    def test_default_case(self):
        result=evaluate(cases()[0]); self.assertIn('metrics',result); self.assertIn('output',result)
    def test_determinism(self):
        case=json.loads(cases()[0].read_text()); a=run_case(case); b=run_case(case)
        self.assertEqual(a['metrics'],b['metrics'])
