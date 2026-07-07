# Testing

Run `python scripts/run_tests.py`. Tests cover algorithms, invalid inputs, invariants, CLI behavior, JSON handling and 36 workloads.
Workload oracles are specification files, not copies of output. They assert conservation, correctness and failure handling.
Use `scripts/verify.py` to audit the 165 tracked files; generated caches and local build results are excluded.
Optional-runtime tests are marked separately and must not be described as passed without execution.

