// 64-bit Linux tracepoint reference. Verify layout with the running kernel tracefs format.
#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>
struct enter_context { __u64 common; __s64 syscall_number; __u64 args[6]; };
struct event { __u64 timestamp; __u64 pid_tgid; __u32 current_uid; __u32 target_uid; };
struct { __uint(type,BPF_MAP_TYPE_RINGBUF); __uint(max_entries,1<<20); } events SEC(".maps");
SEC("tracepoint/syscalls/sys_enter_setuid") int observe_setuid(struct enter_context *ctx){
    __u32 current_uid=(__u32)bpf_get_current_uid_gid(),target=(__u32)ctx->args[0];
    if(target==0&&current_uid!=0){
        struct event *event=bpf_ringbuf_reserve(&events,sizeof(*event),0);if(!event)return 0;
        event->timestamp=bpf_ktime_get_ns();event->pid_tgid=bpf_get_current_pid_tgid();event->current_uid=current_uid;event->target_uid=target;bpf_ringbuf_submit(event,0);
    }
    return 0;
}
char LICENSE[] SEC("license")="GPL";
