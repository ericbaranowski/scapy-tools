from scapy.all import *
def show_packet(packet):
	print(packet.summary())
sniff(filter="tcp port 80",iface="wlan0",prn=show_packet,timeout=60)
