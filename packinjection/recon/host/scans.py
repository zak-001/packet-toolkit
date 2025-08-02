#scanme.nmap.org
from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.sendrecv import sr
def tcp_syn_scan(hosts):
    ans, _ = sr(IP(dst=hosts)/TCP(dport=80, flags='S'))
    ans.summary()
#if syn/ack send rst

def tcp_ack_scan(hosts):
    ans, _ = sr(IP(dst=hosts)/TCP(dport=80, flags='A'))
    ans.summary()
#tcp_syn_scan("scanme.nmap.org")
#tcp_ack_scan("scanme.nmap.org")

#add if logic with up/down message
def udp_scan(hosts):
    ans, _ = sr(IP(dst=hosts)/UDP(dport=[0,1,4,7,9]),timeout=3)
    ans.summary()
#udp_scan("scanme.nmap.org")

protocols = {
    1: ICMP(),      # ICMP
    6: TCP(dport=80),  # TCP (HTTP)
    17: UDP(dport=53), # UDP (DNS)
    47: GRE(),      # GRE
    50: ESP(),      # IPSec ESP
    51: AH(),       # IPSec AH
    115: L2TP()     # L2TP
}
def ip_scan(hosts):
    ans,_=sr([
    IP(dst=hosts, proto=proto)/header 
    for proto, header in protocols.items()
], timeout=3)
    ans.summary()
ip_scan("scanme.nmap.org")
