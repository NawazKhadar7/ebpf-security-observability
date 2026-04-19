# Explicit test deployment

Compile `kernel/xdp_agent.c` with the BPF target and correct Linux/libbpf include paths. Use `sh scripts/load_agent.sh TEST_IFACE artifacts/xdp_agent.o` to view the plan. Add `--apply` only on a reviewed test interface. Detach with `ip link set dev TEST_IFACE xdp off`.

The script attaches but does not pin/update maps. To populate the deny map, identify its map ID using bpftool, pin it to a private bpffs location and use the control helper's update command. The setuid program requires a separate tracepoint loader/ring-buffer reader; neither is bundled. Trace layout must be checked against tracefs on the target 64-bit kernel. No native execution has occurred here.
