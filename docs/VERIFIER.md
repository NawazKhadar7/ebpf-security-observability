# Verifier checks

Build with clang -O2 -g -target bpf and libbpf development headers on a Linux test machine. Verify every packet access is dominated by a bounds check. Capture verifier logs and test on the intended kernel; source inspection is not proof of verifier acceptance.
