# Limitations

No BPF compiler, libbpf headers, bpftool or privileged kernel attachment was available. Kernel programs are uncompiled/unverified sources. Python policy is global per source; native rate buckets are per CPU, so multi-CPU aggregate limits differ. Setuid tracing observes attempts, not successful unauthorized privilege escalation. VLAN, IPv6 and checksum enforcement are not implemented; non-IPv4 traffic passes.
