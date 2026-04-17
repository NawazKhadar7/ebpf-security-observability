# burst-above

Send nine packets from one source.

Exactly the ninth packet exceeds the threshold.

Family: bursts. Size: 9. Deterministic seed: 910308.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case burst-above
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| packets | equals 9 |
| passed | equals 8 |
| denied | equals 0 |
| malformed | equals 0 |
| rate_dropped | equals 1 |
| accounted | equals true |
| kernel_attached | equals false |

Scope: Python packet policy; no kernel programs are attached.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
