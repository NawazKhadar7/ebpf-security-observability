# Benchmarks

Run `python scripts/benchmark.py` to obtain measured wall-clock durations and semantic counters.
The result includes Python and OS information. Inputs are synthetic and the harness includes setup and oracle checking.
These are end-to-end reference timings, not isolated kernel latency or production capacity. Use warmup, repeated trials,
percentiles, hardware details and external load generation for a formal performance study. No target throughput is asserted.

