#!/usr/bin/env python3

from ipaddress import ip_address, IPv4Address, IPv6Address

# for ip4 in ipv4list:
#     if type(ip_address(ip4)) == IPv4Address:
#         print(f"{ip4} is a valid IPv4 address!")
# 
# for ip6 in ipv6list:
#    print(ip_address(ip6))

ipchk = input('Apply an IP address: ') # this line now prompts the user for input

if ipchk == '192.168.70.1': # if a match on '192.168.70.1'
   # indented under if
   print('Looks like the IP address of the Gateway was set: ' + ipchk + ' This is not recommended.')
elif ( type(ip_address(ipchk)) == IPv4Address ) or ( type(ip_address(ipchk)) == IPv6Address ):

   # IPv4 Address Check
   try:
       type(ip_address(ipchk)) == IPv4Address
       print(f"{ipchk} is a valid IPv4 address!") 
   except:
       # Do nothing but don't error out
       print("nothing")

   # IPv6 Address Check 
   try:
       type(ip_address(ipchk)) == IPv6Address
       print(f"{ipchk} is a valid IPv6 address!") 
   except:
       # Do nothing but don't error out
       print("nothing2")

else: # if data is NOT provided
   print('You did not provide input.') # indented under else




