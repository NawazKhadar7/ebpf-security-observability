# bursts-016-02

Rate-limit a single source beyond eight packets per window.

Input scale: 16; deterministic random seed: 164.
Run `python scripts/demo.py --case workloads/bursts-016-02.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
