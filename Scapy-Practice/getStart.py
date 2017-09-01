from scapy.all import *

p = IP(dst = 'koyama.me') / TCP(dport = 80) / Raw(b'00000000')
sr1(p)

'''
this is sample code on official web site
'''
