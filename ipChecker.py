#!/usr/bin/python3 

from ipaddress import ip_address, IPv4Address, IPv6Address

from Chad Feeser to Everyone:    11:33  AM

for ip4 in ipv4list:
    if type(ip_address(ip4)) == IPv4Address:
        print(f"{ip4} is a valid IPv4 address!")

for ip6 in ipv6list:
    print(ip_address(ip6))
