#! /usr/bin/env python3

from scapy.all import *

target = "192.168.56.105"  # Replace with target IP
port = 80               # Common port (adjust if needed)

# Step 1: SYN
syn = IP(dst=target)/TCP(dport=port, flags="S", seq=100)
syn_ack = sr1(syn, timeout=2)

# Step 2: ACK (complete handshake)
ack = IP(dst=target)/TCP(dport=port, flags="A", seq=101, ack=syn_ack[TCP].seq + 1)
send(ack, verbose=0)

# Craft a segment with NO FLAGS (flags=0) + payload
null_payload = IP(dst=target)/TCP(dport=port, flags="", seq=101, ack=syn_ack[TCP].seq + 1)/Raw(load="Linux?")
reply = sr1(null_payload, timeout=5)

# Analyze response
if reply and reply.haslayer(TCP):
    if reply[TCP].flags & 0x10:  # ACK flag set (Linux behavior)
        print(f"[+] {target} is likely Linux (ACKs NULL+payload)")
    elif reply[TCP].flags & 0x04:  # RST (Windows/BSD)
        print(f"[+] {target} is non-Linux (rejects NULL+payload)")
else:
    print("[-] No response (filtered or unexpected behavior)")
