// Original XDP reference; requires Linux headers and libbpf development headers.
#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_endian.h>
struct bucket { __u64 stamp; __u64 packets; };
struct { __uint(type,BPF_MAP_TYPE_HASH); __uint(max_entries,1024); __type(key,__u32); __type(value,__u8); } denylist SEC(".maps");
struct { __uint(type,BPF_MAP_TYPE_LRU_PERCPU_HASH); __uint(max_entries,4096); __type(key,__u32); __type(value,struct bucket); } rates SEC(".maps");
struct { __uint(type,BPF_MAP_TYPE_PERCPU_ARRAY); __uint(max_entries,4); __type(key,__u32); __type(value,__u64); } counters SEC(".maps");
static __always_inline int count_action(__u32 reason,int verdict){
    __u64 *value=bpf_map_lookup_elem(&counters,&reason);if(value)(*value)++;return verdict;
}
SEC("xdp") int xdp_agent(struct xdp_md *ctx){
    void *data=(void*)(long)ctx->data,*end=(void*)(long)ctx->data_end;
    struct ethhdr *eth=data;if((void*)(eth+1)>end)return count_action(3,XDP_DROP);
    if(eth->h_proto!=bpf_htons(ETH_P_IP))return count_action(0,XDP_PASS);
    struct iphdr *ip=(void*)(eth+1);if((void*)(ip+1)>end)return count_action(3,XDP_DROP);
    __u32 ihl=ip->ihl*4,total=bpf_ntohs(ip->tot_len);
    if(ip->version!=4||ihl<20||total<ihl||(void*)ip+ihl>end||(void*)ip+total>end)return count_action(3,XDP_DROP);
    __u32 source=ip->saddr;__u8 *denied=bpf_map_lookup_elem(&denylist,&source);if(denied&&*denied)return count_action(1,XDP_DROP);
    __u64 now=bpf_ktime_get_ns();struct bucket *value=bpf_map_lookup_elem(&rates,&source);
    if(!value){struct bucket first={now,1};bpf_map_update_elem(&rates,&source,&first,BPF_ANY);return count_action(0,XDP_PASS);}
    if(now-value->stamp>=1000000000ULL){value->stamp=now;value->packets=0;}
    value->packets++;if(value->packets>8)return count_action(2,XDP_DROP);
    return count_action(0,XDP_PASS);
}
char LICENSE[] SEC("license")="GPL";
