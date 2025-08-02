#! /usr/bin/env python3

from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr
import logging
from packinjection.utils import select_iface
def ping_sweep(ip_range, iface=None):
    if iface == None:
        iface = select_iface()
    logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
    ans,_= sr(IP(dst=ip_range)/ICMP(),timeout=0.3)
    ans.summary()

ping_sweep("192.168.56.100/30")
#add no hosts found
