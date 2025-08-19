#! /usr/bin/env python3

# Idea: Send packets with incorrect checksums.
# Some IDS/IPS only inspect them, but target OS discards them → noise/IDS evasion.

# what i see: give a bunch of garbage to IDS/ hide indide garbage

from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send

def bad_checksum(target_ip, target_port=80):
    pkt = IP(dst=target_ip) / TCP(dport=target_port, flags="S")
    pkt[TCP].chksum = 0x1234  # bad checksum
    send(pkt, verbose=False)

if __name__ == "__main__":
    bad_checksum("192.168.1.10")

