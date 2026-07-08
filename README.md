# eBPF Network Observability & Security Agent

A packet-policy reference with original XDP filtering and setuid tracepoint source plus a deliberate dry-run deployment workflow.

## 1. Overview

Packet-policy experiments need exact accounting and a clear distinction between a userspace model and a loaded kernel program. This project provides a runnable packet parser/policy reference plus separate XDP and tracepoint sources for later kernel validation.

**Project type:** educational reference implementation. **Repository contents:** 165 non-empty source, test, configuration, workload and documentation files, including 36 synthetic workload scenarios.

## 2. Core Features — Why They Matter

- **Packet reference model:** Builds/parses binary Ethernet and IPv4 packets for deterministic policy tests.
- **Policy and counters:** Applies deny/rate rules and records pass, malformed and drop decisions.
- **Native XDP source:** Includes bounds checks, maps, per-CPU rate buckets and action counters.
- **Observability and control:** Includes setuid-attempt tracepoint source and explicit dry-run attachment plans.

## 3. Tech Stack & Architecture

| Layer | Technology | Implementation status |
| --- | --- | --- |
| Default execution | Python 3.10+ packet/policy reference | Runnable without kernel attachment |
| Optional kernel path | C eBPF/XDP, BPF compiler and libbpf headers | Sources included; not compiled or verifier-tested in bundle validation |
| Optional deployment | bpftool, iproute2 and a suitable Linux test environment | Dry-run planning by default; kernel attachment not exercised |

### How the components fit together

The Python reference parses Ethernet/IPv4 bytes and applies policy before updating counters. The separate native XDP path uses maps and verdicts; a tracepoint emits setuid-attempt events to a ring buffer. User-space control constructs explicit deployment plans.

| Component | Responsibility |
| --- | --- |
| [src/syslab/packet.py](src/syslab/packet.py) | Binary packet construction and parsing. |
| [src/syslab/policy.py](src/syslab/policy.py) | Reference deny/rate rules and counters. |
| [kernel/xdp_agent.c](kernel/xdp_agent.c) | Native XDP packet policy source. |
| [kernel/syscall_monitor.c](kernel/syscall_monitor.c) | Native setuid-attempt tracepoint source. |

See [Architecture](docs/ARCHITECTURE.md) and [Algorithms](docs/ALGORITHMS.md) for implementation notes.

### Scope and limitations

No BPF compiler, libbpf headers, bpftool or privileged kernel attachment was available. Kernel programs are uncompiled/unverified sources. Python policy is global per source; native rate buckets are per CPU, so multi-CPU aggregate limits differ. Setuid tracing observes attempts, not successful unauthorized privilege escalation. VLAN, IPv6 and checksum enforcement are not implemented; non-IPv4 traffic passes.

## 4. Getting Started / Installation

**Prerequisites:** Python 3.10+. The default reference uses Python's standard library. No API keys or external services are needed for the default sample.

Download/extract this project or clone its repository, then open a terminal in the `ebpf-security-observability` folder. Create an isolated environment:

```sh
python -m venv .venv
```

Activate it on Linux/macOS:

```sh
source .venv/bin/activate
```

Or on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the declared Python dependencies and run the demo:

```sh
python -m pip install -r requirements.txt
python scripts/demo.py
```

Check behavior and collect timings on your own machine:

```sh
python scripts/run_tests.py
python scripts/benchmark.py
```

The original bundle validation recorded **22 passing tests** for this project and **36 accepted workload scenarios**. These are local reference checks, not production or hardware benchmarks. See [Testing](docs/TESTING.md) and [Benchmark notes](docs/BENCHMARKS.md).

## 5. Usage Examples

### Run a reproducible workload

The bundled [sample request](examples/request.json) contains:

```json
{
  "family": "allow",
  "id": "allow-008-01",
  "seed": 101,
  "size": 8
}
```

Run the corresponding workload and check its independent acceptance conditions:

```sh
python scripts/demo.py --case workloads/allow-008-01.case.json
```

Expected `metrics` excerpt from the verified local run; the complete JSON also includes `output`:

```json
{
  "metrics": {
    "accounted": true,
    "denied": 0,
    "kernel_attached": false,
    "malformed": 0,
    "packets": 8,
    "passed": 8,
    "rate_dropped": 0
  }
}
```

Eight packets pass the Python policy and all packets are accounted for. kernel_attached=false means no eBPF program is loaded by this example and no kernel performance is measured.

The complete example is in [examples/response.json](examples/response.json). Floating-point last digits can vary across numeric environments.

### Explore through the local dashboard

```sh
python scripts/serve.py --port 8080
```

Open [http://127.0.0.1:8080](http://127.0.0.1:8080), select a workload and choose **Run and check**. The server listens on loopback and is intended for local inspection.

With the server running, a second terminal can call its workload inspection API:

```sh
curl "http://127.0.0.1:8080/api/run?id=allow-008-01"
```

This endpoint executes the bundled workload; it is not a production domain API.

## 6. Your Contributions / Research Alignment

### Implementation evidence

The following work areas are present in this reference and can be reviewed directly:

| Work area in this reference | Repository evidence |
| --- | --- |
| Packet reference model | [src/syslab/packet.py](src/syslab/packet.py) |
| Correctness and edge cases | [tests/](tests/) and [acceptance workloads](workloads/) |
| Reproducible evaluation | [scripts/demo.py](scripts/demo.py), [scripts/benchmark.py](scripts/benchmark.py), [testing notes](docs/TESTING.md) |

### Research alignment

The project connects operating systems, network policy and security observability. Its research value lies in checking policy equivalence, understanding per-CPU state and measuring kernel overhead after actual validation.

**A question to investigate:** How do per-CPU rate buckets differ from a global policy under multicore load, and what overhead does verified instrumentation add?

This question is a proposed extension, not a completed research result. Evaluate it with controlled inputs, independent correctness checks and measurements tied to a reproducible configuration.

### Personal contribution record

This reference was generated from the supplied project concept. Personal authorship or research contributions have not been verified. For an MS application, document only the modules you actually changed, the design choices you can explain, and experiments you ran; link those claims to commits or reproducible reports. See [Provenance](docs/PROVENANCE.md).

All bundled inputs are synthetic. The repository does not establish historical development dates, prior deployment or published research.
