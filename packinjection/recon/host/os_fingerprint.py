#! /usr/bin/env python3

from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send, sr1

#import tcp connect if better
def linux(target,port=80):
	syn = IP(dst=target)/TCP(dport=port, flags="S", seq=100)
#	print(f"1 : me->him : SYN : seq={syn.seq}, ack={syn.ack}")
	ans = sr1(syn, timeout=1)
#	ans.show2()
	r_seq = ans[TCP].seq
	ack = IP(dst=target)/TCP(dport=port, flags="A", seq=101, ack=r_seq+1)
#	ack.show2()
	send(ack)
	a = sr1(IP(dst=target)/TCP(dport=port, flags=0, seq=101, ack=r_seq+1)/b"fingerprint", timeout=2)
	a.show2()
	print(f"1 : me->him : {syn[TCP].flags} : seq={syn.seq}, ack={syn.ack}")
	print(f"2 : him->me : {ans[TCP].flags} : seq={ans.seq}, ack={ans.ack}")
	print(f"3 : me->him : {ack[TCP].flags} : seq={ack.seq}, ack={ack.ack}")
	print(f"2 : him->me : {a[TCP].flags} : seq={a.seq}, ack={a.ack}")
#	test = IP(dst=target)/TCP(dport=port, flags="", seq=101, ack=r_seq+1)/"payload"
#	ans2 = sr1(test, timeout=1)
#	ans2.show2()
linux("192.168.56.105")
#linux("scanme.nmap.org")


#add response logic (if ack/rst) otherwise it will break if not linux
