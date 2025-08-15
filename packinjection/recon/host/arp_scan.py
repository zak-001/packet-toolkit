#! /usr/bin/env python3

from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp
#from scapy.layers.l2 import arping
from packinjection.utils.inet import select_iface

def scan(network="192.168.1.0/24", interface=None, timeout=3, result=None, verbose=2):
	if interface is None:
		interface = select_iface(network)
	ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=network), iface=interface, timeout=timeout, verbose=verbose)
	if result == None:
		ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%") )
	hosts = []
	if result == "1mac":
		for s,r in ans:
                	hosts = r[Ether].src
	else:
		for s,r in ans:
			hosts.append((r[Ether].src, r[ARP].psrc))

	return hosts

#print(conf.route, conf.iface)
#a=scan("192.168.56.0/24")
#print(a)
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
