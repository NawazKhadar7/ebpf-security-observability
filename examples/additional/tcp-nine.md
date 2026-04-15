# tcp-nine

Pass nine TCP packets from distinct sources.

Transport selection must preserve packet accounting.

Family: tcp. Size: 9. Deterministic seed: 910305.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case tcp-nine
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| packets | equals 9 |
| passed | equals 9 |
| denied | equals 0 |
| malformed | equals 0 |
| rate_dropped | equals 0 |
| accounted | equals true |
| kernel_attached | equals false |

Scope: Python packet policy; no kernel programs are attached.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
