#! /usr/bin/env python3

# Idea: Use low TTL so packets expire before reaching destination.
# IDS sitting before the target sees them, but the host never does.
# Can also randomize TTL to confuse detection.

# what i see: confusing investigation (different logs(IDS vs endpoint))

from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send
# add choosing ttl not ips
def ttl_evasion(target_ip, target_port=80):
    pkt = IP(dst=target_ip, ttl=2) / TCP(dport=target_port, flags="S")
    send(pkt, verbose=False)

if __name__ == "__main__":
    ttl_evasion("192.168.1.10")

