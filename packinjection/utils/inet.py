#! /usr/bin/env python3

from scapy.config import conf
from scapy.route import Route
import netifaces
Route()

def select_iface(ip="0.0.0.0"):
	iface, _, _ = conf.route.route(ip)
	return iface

def get_broadcast_ip(ip="0.0.0.0"):
	iface = select_iface(ip)
	broadcast_ip = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['broadcast']
	return broadcast_ip

def get_gw(ip="0.0.0.0"):
	_, _, gw = conf.route.route(ip)
	return gw

#print(get_gw("192.168.56.106"))
#print(f"Broadcast IP: {get_broadcast_ip('192.168.56.101')}")
#print(conf.route)
#print(conf.route.route("192.168.56.3"))
#print(if_select("192.168.56.0"))
#print(conf.route.route("8.8.8.8"))
