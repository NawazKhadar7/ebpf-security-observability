import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.control import update_command,plan
class ControlTests(unittest.TestCase):
    def test_network_order(self):self.assertEqual(update_command('/map','10.2.3.4')[7:11],['0a','02','03','04'])
    def test_no_shell_interface(self):
        with self.assertRaises(ValueError):plan('eth0; rm -rf /','agent.o')
