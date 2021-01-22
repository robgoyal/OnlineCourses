#!/usr/bin/env python3

import optparse
import scapy.all as scapy


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="ip", help="IP/Subnet to perform a network scan against")

    options, arguments = parser.parse_args()
    if not options.ip:
        parser.error("[-] Please specify an IP Address or a Subnet. Use --help for more info.")
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_request = broadcast/arp_request

    clients_list = []

    answered, unanswered = scapy.srp(arp_broadcast_request, timeout=1, verbose=False)
    for sent, answer in answered:
        clients_list.append({"mac": answer.hwsrc, "ip": answer.psrc})
    return clients_list


def print_result(clients):
    # Output Header
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client in clients:
        print(f"{client['ip']}\t\t{client['mac']}")


def main():
    options = get_arguments()
    clients = scan(options.ip)
    print_result(clients)


if __name__ == "__main__":
    main()
