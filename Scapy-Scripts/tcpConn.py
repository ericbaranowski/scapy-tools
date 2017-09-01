#!/usr/bin/env python

import sys
from scapy.all import *
conf.verb=0

# Varibles
source = sys.argv[1]
target = sys.argv[2]
portNums = [0,0,0,0,0,0,0,0,0,0]

# Begin scan for 10 well known ports
for x in range(0,10):
    # Set random ports at each run
    randomDport = random.randint(0,1023)
    randomSport = random.randint(1024,65535)
    # Test for first run at port 80
    if(x == 0):
        p1=IP(dst=target,src=source)/TCP(dport=80,sport=randomSport,flags='S')
        r1=sr1(p1, inter = random.randint(0,5))
        print "this packet was sent: "
        p1.show()
        print "this was the reply: "
        r1.show()
        # Reset first run
        testPort = 0
        # Test for open closed, print out
        if(r1.getlayer(TCP).flags == 0x12):
            portNums[x]= "Port " + str(r1.getlayer(TCP).sport) + " open!"
        elif(r1.getlayer(TCP).flags == 0x14):
            portNums[x]= "Port " + str(r1.getlayer(TCP).sport) + " closed!"
    # If not first run get the rest of random 10 port
    if(x != 0):
        p1=IP(dst=target,src=source)/TCP(dport=randomDport,sport=randomSport,flags='S')
        r1=sr1(p1, inter = random.randint(0,5))
        print "this packet was sent: "
        p1.show()
        print "this was the reply: "
        r1.show()
        # Reset first run
        testPort = 0
        # Test for open closed, print out
        if(r1.getlayer(TCP).flags == 0x12):
            portNums[x]= "Port " + str(r1.getlayer(TCP).sport) + " open!"
        elif(r1.getlayer(TCP).flags == 0x14):
            portNums[x]= "Port " + str(r1.getlayer(TCP).sport) + " closed!"
        
# Output results for ports
print "TCP connection results: "
for x in range(0,10):
    print portNums[x]

sys.exit(0)
