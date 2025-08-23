#! /usr/bin/env python3

from scapy.layers.inet import IP, UDP, ICMP, TCP
from scapy.layers.dns import DNS, DNSQR
from scapy.sendrecv import sr

def tcp_tracert(target):
	pkt = IP(dst=target, ttl=(1,23))/TCP(dport=53,flags="S")
	ans, _ = sr(pkt, timeout=2, retry=5)
	ans.summary(lambda s,r : f'{s.sprintf("%IP.ttl%")}\t{r.sprintf("%IP.src%")}')

def udp_tracert(target):
        pkt = IP(dst=target, ttl=(1,23))/UDP(sport=33434, dport=33434)/DNS(qd=DNSQR(qname="scanme.nmap.org"))
        ans, _ = sr(pkt, timeout=1, retry=5)
        ans.summary(lambda s,r : f'{s.sprintf("%IP.ttl%")}\t{r.sprintf("%IP.src%")}')

def icmp_tracert(target):
        pkt = IP(dst=target, ttl=(1,23))/ICMP()
        ans, _ = sr(pkt, timeout=2, retry=5)
        ans.summary(lambda s,r : f'{s.sprintf("%IP.ttl%")}\t{r.sprintf("%IP.src%")}')

if __name__ == '__main__' :

	icmp_tracert("scanme.nmap.org")
	tcp_tracert("scanme.nmap.org")
	udp_tracert("scanme.nmap.org")

# can upgrade to look like os ones (three times with time)
