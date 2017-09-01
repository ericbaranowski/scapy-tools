from scapy.all import *

a = IP(ttl=10)

a.src = '127.0.0.1'
a.dst = '192.168.0.40'

del(a.ttl)

