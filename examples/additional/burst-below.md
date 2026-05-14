# burst-below

Send seven packets from one source.

The eight-packet threshold has not been reached.

Family: bursts. Size: 7. Deterministic seed: 910306.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case burst-below
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| packets | equals 7 |
| passed | equals 7 |
| denied | equals 0 |
| malformed | equals 0 |
| rate_dropped | equals 0 |
| accounted | equals true |
| kernel_attached | equals false |

Scope: Python packet policy; no kernel programs are attached.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
