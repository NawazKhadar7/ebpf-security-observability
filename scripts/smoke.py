import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from syslab.cli import cases,evaluate
for path in cases(): evaluate(path)
print('36 workload oracles passed')
