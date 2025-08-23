#! /usr/bin/env python3

from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr
import logging


def ping_sweep(ip_range):
    if '-' in ip_range:
        base, iprange = ip_range.rsplit('.',1)
        start,end = map(int, iprange.split('-'))
        pkt = IP(dst=[f"{base}.{i}" for i in range(start, end+1)])/ICMP()
    else :
        pkt = IP(dst=ip_range)/ICMP()
    logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
    ans,_= sr(pkt, timeout=0.3)
    ans.summary(lambda s,r: r.sprintf("[+] %IP.src% is up") )
    if not ans:
        print("[-] All hosts are down")

if __name__ == '__main__' :
	ping_sweep("192.168.56.100-110")
# make a global ip parser for - notation

