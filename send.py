#!/usr/bin/python 
from scapy.all import *
import pdb

nic_name="lo"

def fake_icmp(vlan_id):
    #arp_pkt = Ether(dst="FF:FF:FF:FF:FF:FF")/Dot1Q(vlan=int('%d'%vlan_id))/ARP(pdst="1.1.1.1")
    icmp_pkt = Ether(dst="FF:FF:FF:FF:FF:FF")/Dot1Q(vlan=int('%d'%vlan_id))/IP(dst="1.1.1.2",src="1.1.1.1",proto=1)/ICMP()
    sendp(icmp_pkt,iface=nic_name,inter=0.01)

def main():
    for vlan_id in range(1,4095):
        fake_icmp(vlan_id)

if __name__ == "__main__":
    main()
