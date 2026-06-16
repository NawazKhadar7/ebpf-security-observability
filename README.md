# eBPF Network Observability & Security Agent

A packet-policy reference with original XDP filtering and setuid tracepoint source plus a deliberate dry-run deployment workflow.

This is newly generated educational reference code based on a concept in the supplied PDF.
It has **165 non-empty source, test, configuration, workload and documentation files**.
It is a prototype for study and extension, not evidence of previous deployment or measured large-scale performance.

## Quick start

Requires Python 3.10+; the default path uses the standard library.

```sh
python scripts/demo.py
python scripts/run_tests.py
python scripts/benchmark.py
python scripts/serve.py --port 8080
```

Open http://127.0.0.1:8080 for the workload dashboard. `scripts/demo.py --case workloads/<id>.case.json`
executes one workload and checks its independent acceptance conditions. `benchmark.py` prints actual local timings.

## Implemented scope

Python binary packet builder/parser, deny/rate policy and exact counters. Native C XDP bounds checks, deny map, per-CPU LRU rate buckets, action counters and setuid-attempt ring-buffer tracepoint. Control helpers produce argument-safe bpftool/ip plans.

## Limits and optional runtimes

No BPF compiler, libbpf headers, bpftool or privileged kernel attachment was available. Kernel programs are uncompiled/unverified sources. Python policy is global per source; native rate buckets are per CPU, so multi-CPU aggregate limits differ. Setuid tracing observes attempts, not successful unauthorized privilege escalation. VLAN, IPv6 and checksum enforcement are not implemented; non-IPv4 traffic passes.

All bundled data are synthetic. No credentials, pretrained model weights, historical commits, or fabricated benchmark results are included.
See `docs/PROVENANCE.md`, `docs/TESTING.md`, and the bundle's validation report for evidence and omissions.
