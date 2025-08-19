#! /usr/bin/env python3

# Hides between fake ips

# to me: find a way to make an add-on not a stand-alone

# this is a prototype: should auto get my ip and random fake ips with desired number
'''
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send

def decoy_scan(target_ip, target_port=80, decoys=None):
    if decoys is None:
        decoys = ["10.0.0.2", "10.0.0.3"]

    for src in decoys + ["192.168.1.100"]:  # last = real attacker
        pkt = IP(dst=target_ip, src=src) / TCP(dport=target_port, flags="S")
        send(pkt, verbose=False)

if __name__ == "__main__":
    decoy_scan("192.168.1.10")
'''
