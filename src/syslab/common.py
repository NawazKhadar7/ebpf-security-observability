"""Shared reproducibility helpers; no external services or credentials required."""
import json, math, os, tempfile
from pathlib import Path

def validate_case(case):
    if not isinstance(case,dict): raise ValueError('case must be an object')
    for k in ('id','family','size','seed'):
        if k not in case: raise ValueError('missing '+k)
    if not isinstance(case['id'],str) or not case['id']: raise ValueError('invalid id')
    if not isinstance(case['family'],str): raise ValueError('invalid family')
    for k in ('size','seed'):
        if isinstance(case[k],bool) or not isinstance(case[k],int): raise ValueError(k+' must be an integer')
    if not 1 <= case['size'] <= 10000: raise ValueError('size outside 1..10000')
    if not 0 <= case['seed'] < 2**32: raise ValueError('seed outside uint32')
    return case

def check(result, expected):
    """Independent assertions specified in workload oracle files."""
    metrics=result['metrics']; errors=[]
    for name, rule in expected['checks'].items():
        if name not in metrics: errors.append('missing metric '+name); continue
        value=metrics[name]
        for op, target in rule.items():
            ok={'equals':lambda:value==target,'min':lambda:value>=target,'max':lambda:value<=target}[op]()
            if not ok: errors.append(f'{name}: {value!r} violates {op} {target!r}')
    if errors: raise AssertionError('; '.join(errors))
    return True

def dumps(value): return json.dumps(value,sort_keys=True,allow_nan=False)

def atomic_json(path,value):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(dir=path.parent,prefix='.write-')
    try:
        with os.fdopen(fd,'w') as f:
            f.write(dumps(value)+'\n'); f.flush(); os.fsync(f.fileno())
        os.replace(tmp,path)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)

def finite_numbers(values):
    if not all(isinstance(v,(int,float)) and math.isfinite(v) for v in values):
        raise ValueError('numbers must be finite')
    return values
