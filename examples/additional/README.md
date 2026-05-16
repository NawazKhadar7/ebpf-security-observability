# Additional scenarios for ebpf-security-observability

Ten runnable scenarios cover small inputs, odd sizes, and behavior boundaries in the existing reference implementation.

This directory contains 10 input JSON files, 10 metric-oracle JSON files, 10 scenario notes, this guide, and the runner (32 files).

Run from the project directory with Python 3.10 or later and the dependencies already listed in requirements.txt.

~~~powershell
python -B examples/additional/run_cases.py --list
python -B examples/additional/run_cases.py
python -B examples/additional/run_cases.py --case allow-single --json
~~~

The runner exits with zero only when all selected scenarios pass. --json includes metrics and output or a failure reason for each scenario.

Each .case.json is paired with a .expected.json containing equality checks or numeric bounds for the existing syslab.common.check helper.
Scenario notes explain the selected boundaries. Fixed seeds make inputs repeatable; expected files contain assertions rather than recorded timings.

| Scenario | Family | Size | Purpose |
| --- | --- | --- | --- |
| allow-single | allow | 1 | Pass one valid IPv4 packet. |
| deny-single | deny | 1 | Reject one packet from the denied source. |
| malformed-single | malformed | 1 | Reject one truncated packet. |
| udp-seven | udp | 7 | Pass seven UDP packets from distinct sources. |
| tcp-nine | tcp | 9 | Pass nine TCP packets from distinct sources. |
| burst-below | bursts | 7 | Send seven packets from one source. |
| burst-exact | bursts | 8 | Send exactly eight packets from one source. |
| burst-above | bursts | 9 | Send nine packets from one source. |
| burst-seventeen | bursts | 17 | Send seventeen packets within one rate window. |
| source-rollover | allow | 251 | Generate 251 distinct IPv4 sources. |

Scope: Python packet policy; no kernel programs are attached.

Supplemental inputs have their own runner, so the existing workload discovery and its 36-case suite retain their current behavior.
Bytecode generation is disabled. Reports go to standard output; storage and model artifacts use the reference code's temporary directories.

See [limitations](../../docs/LIMITATIONS.md) and [running instructions](../../docs/RUNNING.md).
