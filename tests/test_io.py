import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
class IoTests(unittest.TestCase):
    def test_atomic_replacement(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'state.json'; atomic_json(path,{'v':1}); atomic_json(path,{'v':2})
            self.assertEqual(json.loads(path.read_text()),{'v':2}); self.assertEqual(len(list(Path(tmp).iterdir())),1)
    def test_json_is_finite(self):
        with self.assertRaises(ValueError): dumps({'bad':float('nan')})
