# allow-single

Pass one valid IPv4 packet.

The packet must increment exactly one pass counter.

Family: allow. Size: 1. Deterministic seed: 910301.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case allow-single
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| packets | equals 1 |
| passed | equals 1 |
| denied | equals 0 |
| malformed | equals 0 |
| rate_dropped | equals 0 |
| accounted | equals true |
| kernel_attached | equals false |

Scope: Python packet policy; no kernel programs are attached.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
