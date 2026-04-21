import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.packet import parse,build_ipv4,checksum
class PacketTests(unittest.TestCase):
    def test_roundtrip(self):
        packet=build_ipv4('10.2.3.4');info=parse(packet);self.assertEqual(info['source'],'10.2.3.4');self.assertEqual(checksum(packet[14:34]),0)
    def test_bounds(self):
        for length in (0,13,20,33):
            with self.assertRaises(ValueError):parse(build_ipv4()[:length])
