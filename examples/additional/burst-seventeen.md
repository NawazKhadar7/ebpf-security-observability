# burst-seventeen

Send seventeen packets within one rate window.

Eight pass and the remaining nine are rate-dropped.

Family: bursts. Size: 17. Deterministic seed: 910309.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case burst-seventeen
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| packets | equals 17 |
| passed | equals 8 |
| denied | equals 0 |
| malformed | equals 0 |
| rate_dropped | equals 9 |
| accounted | equals true |
| kernel_attached | equals false |

Scope: Python packet policy; no kernel programs are attached.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
