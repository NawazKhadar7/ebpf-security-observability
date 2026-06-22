# source-rollover

Generate 251 distinct IPv4 sources.

The address generator changes subnet after 250 packets.

Family: allow. Size: 251. Deterministic seed: 910310.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case source-rollover
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| packets | equals 251 |
| passed | equals 251 |
| denied | equals 0 |
| malformed | equals 0 |
| rate_dropped | equals 0 |
| accounted | equals true |
| kernel_attached | equals false |

Scope: Python packet policy; no kernel programs are attached.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
