#!/usr/bin/env python

import sys
from scapy.all import *
conf.verb=0

# Varibles
source = sys.argv[1]
target = sys.argv[2]

# Begin scan for 10 well known ports
for x in range(0,10):
    # Test for first run at port 80
    if(x == 0):
        randomDport = 80
        # Set random ports at each run
        randomSport = random.randint(1024,65535)
        p1=IP(dst=target,src=source)/TCP(dport=80,sport=randomSport,flags='UFP')
        ans,unans=sr(p1,inter=0.1,timeout=3)
        print"this packet was received!"
        ans.show()
        p1.show()
        unans.show()
        print"this packet was replied"
        unans.display()
    elif(x != 0):
        # Set random ports at each run
        randomDport = random.randint(0,1023)
        randomSport = random.randint(1024,65535)
        p1=IP(dst=target,src=source)/TCP(dport=randomDport,sport=randomSport,flags='UFP')
        ans,unans=sr(p1,inter=0.1,timeout=3)
        print"this packet was received!"
        ans.show()
        print"this packet was not replied"
        unans.display()
      
        

sys.exit(0)
