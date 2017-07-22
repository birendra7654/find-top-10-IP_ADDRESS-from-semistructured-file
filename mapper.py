#!/usr/bin/env python
import sys
import string
import re
import socket
import re

def valid_ip(address):
    try: 
        socket.inet_aton(address)
        return True
    except:
        return False

ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";

for line in sys.stdin:
    line = line.strip()
    line = re.sub("\s+", " ", line)
    # print line
    
    line = line.split(" ")
    # print line
    # break
    for i in line:
        if re.match(ValidIpAddressRegex, i):
            print '%s\t%d' % (i, 1)
            break
    
