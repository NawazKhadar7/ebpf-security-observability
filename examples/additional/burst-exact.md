# burst-exact

Send exactly eight packets from one source.

The threshold packet itself must pass.

Family: bursts. Size: 8. Deterministic seed: 910307.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case burst-exact
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| packets | equals 8 |
| passed | equals 8 |
| denied | equals 0 |
| malformed | equals 0 |
| rate_dropped | equals 0 |
| accounted | equals true |
| kernel_attached | equals false |

Scope: Python packet policy; no kernel programs are attached.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
