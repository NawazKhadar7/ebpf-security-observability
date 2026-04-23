# deny-single

Reject one packet from the denied source.

Deny matching takes effect before rate accounting.

Family: deny. Size: 1. Deterministic seed: 910302.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case deny-single
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| packets | equals 1 |
| passed | equals 0 |
| denied | equals 1 |
| malformed | equals 0 |
| rate_dropped | equals 0 |
| accounted | equals true |
| kernel_attached | equals false |

Scope: Python packet policy; no kernel programs are attached.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
