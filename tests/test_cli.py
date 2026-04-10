import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
class CliTests(unittest.TestCase):
    def test_success_json(self):
        import subprocess
        p=subprocess.run([sys.executable,str(ROOT/'scripts/demo.py')],capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stderr); self.assertIn('metrics',json.loads(p.stdout))
    def test_invalid_path(self):
        import subprocess
        p=subprocess.run([sys.executable,str(ROOT/'scripts/demo.py'),'--case','does-not-exist.json'],capture_output=True,text=True)
        self.assertNotEqual(p.returncode,0)
