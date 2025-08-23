#! /usr/bin/env python3

from scapy.layers.inet import IP, UDP
from scapy.sendrecv import sr1

def udp_scan(hosts):
    ans = sr1(IP(dst=hosts)/UDP(dport=[0,1,4,7,9]),timeout=3)
    print(f"{ans[IP].src} is UP")
    #ans.summary(lambda s,r : r.sprintf("%IP.src% is UP"))

if __name__ == '__main__' :
	udp_scan("scanme.nmap.org")
