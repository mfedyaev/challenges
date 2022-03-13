# Convert IP to number and back

def iptonum(ip):
    numbin = ""
    for octet in ip.split("."):
        numbin += bin(int(octet)).replace("0b","").zfill(8)
    return int(numbin, 2)

def numtoip(num):
    numbin = bin(num).replace("0b","")
#    print(f'binary: {numbin}')
    nums = [numbin[i:i+8] for i in range(0,len(numbin),8)]
#    print(nums)
    ip = ""
    i = 0
    for octet in nums:
        while i < 3:
            ip += str(int(octet,2)) + "."
            i += 1
        ip += str(int(octet,2))
    return ip

import ipaddress

def iptonum_ipaddr(ip):
    return int(ipaddress.ip_address(ip))

def numtoip_ipaddr(num):
    return ipaddress.ip_address(num)