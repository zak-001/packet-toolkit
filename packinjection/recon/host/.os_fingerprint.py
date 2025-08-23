''' Requires iptables manip or equivalent'''

'''The kernel interferes and sends tcp packet with rest flag set that interfers with the 3 way handshake

#! /usr/bin/env python3

from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send, sr1

#import tcp connect if better
def linux(target,port=4444):
	syn = IP(dst=target)/TCP(dport=port, flags="S", seq=100)
	ans = sr1(syn, timeout=1)
#	ans.show2()
	r_seq = ans[TCP].seq
	ack = IP(dst=target)/TCP(dport=port, flags="A", seq=101, ack=r_seq+1)
	send(ack)
	a = sr1(IP(dst=target)/TCP(dport=port, flags=0, seq=101, ack=r_seq+1)/b"AACEDBFFF")
	a.show2()

#	print(f"1 : me->him : {syn[TCP].flags} : seq={syn.seq}, ack={syn.ack}")
#	print(f"2 : him->me : {ans[TCP].flags} : seq={ans.seq}, ack={ans.ack}")
#	print(f"3 : me->him : {ack[TCP].flags} : seq={ack.seq}, ack={ack.ack}")
#	print(f"2 : him->me : {a[TCP].flags} : seq={a.seq}, ack={a.ack}")
#	a.show2()
#	if a.haslayer(TCP) and a[TCP].flags & 0x10:
#		b = sr1(IP(dst=target)/TCP(dport=port, flags='R', seq=a[TCP].ack, ack=a[TCP].seq+1), timeout=2)
#		b.show2()
#	else pass/return/wertfgfchgjvh
#	test = IP(dst=target)/TCP(dport=port, flags="", seq=101, ack=r_seq+1)/"payload"
#	ans2 = sr1(test, timeout=1)
#	ans2.show2()

#linux("192.168.56.109")
#linux("scanme.nmap.org")
linux("127.0.0.1", 1234)

#add response logic (if ack/rst) otherwise it will break if not linux

'''
