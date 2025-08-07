#! /usr/bin/env python3
#Inject forged TCP packets with RST flag to terminate sessions.
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send

#sniff or spoof first
def seq_guess(target):
	
