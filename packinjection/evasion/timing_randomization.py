#! /usr/bin/env python3

# Avoid rate-based IDS detection.

import random
import time
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send
# add tiers like nmap
def timing_attack(target_ip, target_port=80, count=10):
    for _ in range(count):
        pkt = IP(dst=target_ip) / TCP(dport=target_port, flags="S")
        send(pkt, verbose=False)
        time.sleep(random.uniform(0.1, 1.0))

if __name__ == "__main__":
    timing_attack("192.168.1.10")
