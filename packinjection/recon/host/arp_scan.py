#! /usr/bin/env python3

from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp
from scapy.config import conf
from scapy.layers.l2 import arping
from packinjection.utils import select_iface
#def get_interface(net="0.0.0.0"):
#	network, netmask, gateway, interface, addr, metric = conf.route.route(net)
#	return interface

def scan(network="192.168.1.0/24", interface=None, timeout=3, verbose=2):
	if interface is None:
		interface = select_iface(network)
	ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=network), iface=interface, timeout=timeout, verbose=verbose)
	ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%") )

#print(conf.route, conf.iface)
scan("192.168.56.0/24")
#arping("192.168.56.0/24")
'''
ip="192.168.0."
answers = []
for i in range(130,150):
    a = ip + str(i)
    print(a)
    answers.append(arp_ping(a))
for ans in answers:
    ans.summary()
'''
