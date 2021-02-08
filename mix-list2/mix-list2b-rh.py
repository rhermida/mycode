#!/usr/bin/env python3

# Original List
proto = ['ssh', 'http', 'https']
print(proto)
print("")

# Effect of APPEND method

proto.append('ftp') # this line will add ftp to the end of our list
print("Effect of APPEND method:")
print(proto)
print("")

# Effect of EXTEND method
print("Effect of EXTEND method:")
proto.extend('dns') # this line will add 'd', 'n', and 's' to the end of our list
print(proto)
print("")

