from .packet import parse
class Policy:
    def __init__(self,deny=(),threshold=8,window_ns=1_000_000_000):
        if threshold<1 or window_ns<1:raise ValueError('positive rate policy required')
        self.deny=set(deny);self.threshold=threshold;self.window=window_ns;self.buckets={};self.counters={'pass':0,'deny':0,'rate':0,'malformed':0}
    def inspect(self,packet,now_ns):
        try:info=parse(packet)
        except ValueError:self.counters['malformed']+=1;return 'malformed'
        if not info['ipv4']:self.counters['pass']+=1;return 'pass'
        source=info['source']
        if source in self.deny:self.counters['deny']+=1;return 'deny'
        stamp,count=self.buckets.get(source,(now_ns,0))
        if now_ns<stamp:raise ValueError('clock must be monotonic')
        if now_ns-stamp>=self.window:stamp,count=now_ns,0
        count+=1;self.buckets[source]=(stamp,count)
        action='rate' if count>self.threshold else 'pass';self.counters[action]+=1;return action
