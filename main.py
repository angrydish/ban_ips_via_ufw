#!/usr/bin/python3

import json
import ipaddress
import sys

nets = json.loads(open('nets.json', 'r').readline())['data']
for network in nets:
	print(f'{network[0]} \t {network[1]} \t {network[2]}', file=sys.stderr)
	for ip_subnet in ipaddress.summarize_address_range(ipaddress.IPv4Address(network[0]),ipaddress.IPv4Address(network[1])):
		print(ip_subnet)
		#print(ip_subnet, " - subnet", file=sys.stderr)
		#for ip in ip_subnet:
		#	print(ip)
		#print(ip_subnet, " - subnet", file=sys.stderr)
	#print(f'{network[0]} \t {network[1]} \t {network[2]}', file=sys.stderr)
	#print([ip for ip in ipaddress.summarize_address_range(ipaddress.IPv4Address(network[0]),ipaddress.IPv4Address(network[1]))])
	#input()
#print([ipaddress.summarize_address_range(ipaddress.IPv4Address(network[0]),ipaddress.IPv4Address(network[1]))])
# 8,388,608
#print(nets[nets.index([i[2] for i in nets].index('8,388,608'))])
#print(nets[[int(elem[2].replace(',', '')) for elem in nets].index(max([int(elem[2].replace(',', '')) for elem in nets]))])
