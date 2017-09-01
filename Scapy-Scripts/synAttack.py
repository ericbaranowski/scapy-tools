#!/usr/bin/env python
import sys
from scapy.all import *
conf.verb=0

x=IP()
x.src = "192.168.56.101"
x.dst = "192.168.56.102"

t=TCP()

p1=x/t

ans,unans=srloop(p1,count=10,inter=0.1)


sys.exit(0)
