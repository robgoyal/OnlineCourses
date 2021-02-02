#!/usr/bin/env python3

import optparse
import kamene.all as scapy

BROADCAST_ADDRESS = "ff:ff:ff:ff:ff:ff:ff"


def get_arguments():
    """
    Return the options:
    - target: IP/Subnet to perform a network scan against
    """

    # Create parser
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="ip", help="IP/Subnet to perform a network scan against")

    # Parse arguments
    options, arguments = parser.parse_args()
    if not options.ip:
        parser.error("[-] Please specify an IP Address or a Subnet. Use --help for more info.")
    return options


def scan(ip):
    """
    Run an ARP scan against the IP/Subnet and return a list of
    clients on the network with their mac address and ip address

    :param ip: str
    :return: list[dict]
    """

    # Create an ARP request destined for the ip/subnet
    arp_request = scapy.ARP(pdst=ip)

    # Create an ethernet frame to the broadcast address
    # REASON: Need to send to the Broadcast address because
    #         the source machine doesn't know who to send the
    #         packet to. Each request is broadcast to the
    #         entire network asking WHOIS <IP ADDRESS>
    broadcast = scapy.Ether(dst=BROADCAST_ADDRESS)

    # Combine the two layers to create an ARP packet
    arp_broadcast_request = broadcast/arp_request

    # Create a list of all responses with their MAC address and IP address
    answered, unanswered = scapy.srp(arp_broadcast_request, timeout=1, verbose=False)
    clients = [{"mac": answer.hwsrc, "ip": answer.psrc} for sent, answer in answered]
    return clients


def print_result(clients):
    """
    Print a formatted table of clients on the network.
    """

    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client in clients:
        print(f"{client['ip']}\t\t{client['mac']}")


def main():
    options = get_arguments()
    clients = scan(options.ip)
    print_result(clients)


if __name__ == "__main__":
    main()
