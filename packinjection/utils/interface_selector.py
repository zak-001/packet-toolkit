#! /usr/bin/env python3

from scapy.config import conf
from scapy.route import Route

Route()

def select_iface(ip="0.0.0.0"):
	iface, _, _ = conf.route.route(ip)
	return iface #, network, gateway
#print(conf.route)
#print(conf.route.route("192.168.56.3"))
#print(if_select("192.168.56.0"))
#print(conf.route.route("8.8.8.8"))
