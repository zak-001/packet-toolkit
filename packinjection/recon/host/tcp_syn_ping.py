#! /usr/bin/env python3

from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.sendrecv import sr, send

def tcp_syn_scan(hosts):
    ans, _ = sr(IP(dst=hosts)/TCP(dport=80, flags='S'), timeout=1)
    for sent_pkt, recv_pkt in ans:
        if recv_pkt.haslayer(TCP) and recv_pkt[TCP].flags == 0x12:  # SYN-ACK (0x12)
            print(f"[+] {recv_pkt[IP].src} is UP")

            # Send RST to close the connection properly
            send(
                IP(dst=recv_pkt[IP].src) / TCP(
                    sport=recv_pkt[TCP].dport,
                    dport=80,
                    seq=recv_pkt[TCP].ack,
                    ack=recv_pkt[TCP].seq + 1,
                    flags="R"
                ),
                verbose=0
            )
            #print(f"[+] Sent RST to {recv_pkt[IP].src}")

    # Print unresponsive hosts (optional)
    '''if unans:
        print("\n[!] No response from:")
        for pkt in unans:
            print(f"    - {pkt[IP].dst}")
    ans.summary(lambda s,r: f"s.haslayer(TCP): {s.haslayer(TCP)}; r.haslayer(TCP):{r.haslayer(TCP)}")
#add if syn/ack send rst
'''
tcp_syn_scan("scanme.nmap.org")
