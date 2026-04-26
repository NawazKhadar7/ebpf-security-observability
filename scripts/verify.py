from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
files=[p for p in root.rglob('*') if p.is_file() and not any(part in {'__pycache__','.venv','.git','artifacts','build'} for part in p.relative_to(root).parts)]
assert len(files)==165, f'expected 165 tracked files, got {len(files)}'
assert all(p.stat().st_size for p in files), 'empty file'
for p in files:
    if p.suffix=='.json': json.loads(p.read_text())
print('165 non-empty files; JSON parsed')
