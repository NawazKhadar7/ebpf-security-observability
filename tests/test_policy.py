import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.policy import Policy
from syslab.packet import build_ipv4
class PolicyTests(unittest.TestCase):
    def test_rate_and_expiry(self):
        p=Policy(threshold=1);packet=build_ipv4();self.assertEqual(p.inspect(packet,0),'pass');self.assertEqual(p.inspect(packet,1),'rate');self.assertEqual(p.inspect(packet,1_000_000_000),'pass')
    def test_deny_precedes_rate(self):
        p=Policy(['10.0.0.1']);self.assertEqual(p.inspect(build_ipv4(),0),'deny');self.assertEqual(p.buckets,{})
