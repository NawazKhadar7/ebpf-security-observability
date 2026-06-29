# Architecture

Reference: Ethernet bytes → IPv4 parser → policy → counters. Native: XDP hook → map policy → verdict; tracepoint → ring buffer. User-space control supplies explicit planned commands.
