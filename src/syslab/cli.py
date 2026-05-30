"""Command line and a loopback-only workload inspection dashboard."""
import argparse, json, sys, time
from pathlib import Path
from .core import run_case
from .common import check, dumps
ROOT=Path(__file__).resolve().parents[2]

def cases(): return sorted((ROOT/'workloads').glob('*.case.json'))

def evaluate(path):
    case=json.loads(path.read_text()); result=run_case(case)
    expected=json.loads((ROOT/'workloads'/(case['id']+'.expected.json')).read_text())
    check(result,expected)
    return result

def main(argv=None):
    parser=argparse.ArgumentParser(description='Reproducible systems reference workloads')
    parser.add_argument('--case',type=Path,default=cases()[0])
    args=parser.parse_args(argv)
    try: print(dumps(evaluate(args.case))); return 0
    except (ValueError,KeyError,AssertionError,OSError) as exc:
        print(str(exc),file=sys.stderr); return 1

def benchmark():
    import platform
    reports=[]
    for path in cases():
        start=time.perf_counter(); result=evaluate(path)
        reports.append({'id':path.stem,'elapsed_ms':round((time.perf_counter()-start)*1000,3),'metrics':result['metrics']})
    print(dumps({'python':platform.python_version(),'platform':platform.platform(),'synthetic':True,'reports':reports}))

def serve(argv=None):
    from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
    from urllib.parse import urlparse,parse_qs
    parser=argparse.ArgumentParser(); parser.add_argument('--port',type=int,default=8080)
    args=parser.parse_args(argv); available={p.name.removesuffix('.case.json'):p for p in cases()}
    html="""<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Systems Workload Explorer</title><style>body{font:16px system-ui;max-width:980px;margin:40px auto;padding:16px;background:#0b1526;color:#e7eef8}button,select{font:inherit;padding:10px}pre{white-space:pre-wrap;background:#17263e;padding:18px}a{color:#8bd5ff}</style><h1>Systems Workload Explorer</h1><p>Local reference implementation · synthetic inputs · measured on your machine.</p><label>Workload <select id="cases"></select></label> <button id="run">Run and check</button><p id="status" role="status"></p><pre id="result">Choose a workload.</pre><script>const list=document.querySelector('#cases'),status=document.querySelector('#status'),out=document.querySelector('#result');fetch('/api/cases').then(r=>r.json()).then(a=>a.forEach(id=>{let o=document.createElement('option');o.value=o.textContent=id;list.append(o)}));document.querySelector('#run').onclick=async()=>{status.textContent='Running…';try{let r=await fetch('/api/run?id='+encodeURIComponent(list.value));let data=await r.json();out.textContent=JSON.stringify(data,null,2);status.textContent=r.ok?'Checks passed':'Run failed'}catch(e){status.textContent=e.message}};</script></html>"""
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            url=urlparse(self.path)
            try:
                if url.path=='/': body=html.encode(); kind='text/html; charset=utf-8'
                elif url.path=='/api/cases': body=dumps(list(available)).encode(); kind='application/json'
                elif url.path=='/api/run':
                    key=parse_qs(url.query).get('id',[''])[0]
                    if key not in available: self.send_error(404); return
                    body=dumps(evaluate(available[key])).encode(); kind='application/json'
                else: self.send_error(404); return
                self.send_response(200); self.send_header('Content-Type',kind)
                self.send_header('Content-Length',str(len(body))); self.send_header('Cache-Control','no-store'); self.end_headers(); self.wfile.write(body)
            except Exception as exc:
                body=dumps({'error':str(exc)}).encode(); self.send_response(500); self.end_headers(); self.wfile.write(body)
        def log_message(self,*args): pass
    server=ThreadingHTTPServer(('127.0.0.1',args.port),Handler)
    print(f'Listening on http://127.0.0.1:{server.server_port}',flush=True)
    try: server.serve_forever()
    except KeyboardInterrupt: pass
    finally: server.server_close()
