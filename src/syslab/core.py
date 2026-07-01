from .common import validate_case
from .packet import build_ipv4
from .policy import Policy
FAMILIES=('allow','deny','bursts','malformed','udp','tcp')
def run_case(case):
    validate_case(case)
    if case['family'] not in FAMILIES:raise ValueError('unknown packet family')
    n=case['size'];f=case['family'];policy=Policy(deny=['10.0.0.9']);actions=[]
    for i in range(n):
        source='10.0.0.9' if f=='deny' else '10.0.0.1' if f=='bursts' else f'10.1.{i//250}.{i%250+1}'
        packet=b'bad' if f=='malformed' else build_ipv4(source,protocol=6 if f=='tcp' else 17);actions.append(policy.inspect(packet,i*1000))
    counters=policy.counters
    return {'metrics':{'packets':n,'passed':counters['pass'],'denied':counters['deny'],'rate_dropped':counters['rate'],'malformed':counters['malformed'],'accounted':sum(counters.values())==n,'kernel_attached':False},'output':{'actions':actions[:16],'execution':'Python packet/policy reference, not in-kernel eBPF'}}
