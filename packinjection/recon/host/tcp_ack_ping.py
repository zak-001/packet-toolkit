#! /usr/bin/env python3

from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr

def tcp_ack_scan(hosts):
    ans, a = sr(IP(dst=hosts)/TCP(dport=[80,443], flags='A'), timeout=1)
    ans.summary(lambda s,r : r.sprintf("%IP.src% is UP"))

if __name__ == '__main__' :
	tcp_ack_scan("scanme.nmap.org")


