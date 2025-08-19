#! /usr/bin/env python3

# add junk padding to bypass signature based detection

# i should change this script:
# - rand junk
# - no packet crafting just add padding (an add-on)

from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send
from scapy.packet import Raw

def padded_attack(target_ip, target_port=80):
    junk = b"X" * 200
    pkt = IP(dst=target_ip) / TCP(dport=target_port, flags="S") / Raw(load=junk)
    send(pkt, verbose=False)

if __name__ == "__main__":
    padded_attack("192.168.1.10")

