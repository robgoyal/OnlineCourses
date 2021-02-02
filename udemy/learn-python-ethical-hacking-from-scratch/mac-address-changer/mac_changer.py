#!/usr/bin/env python

import optparse
import re
import subprocess
import sys


def get_arguments():
    """
    Parse the command line arguments to get the
    interface and mac address as command line args
    """

    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address for")
    parser.add_option("-m", "--mac", dest="new_mac_address", help="New MAC address")

    options, arguments = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    if not options.new_mac_address:
        parser.error("[-] Please specify a new mac address, use --help for more info.")

    return options


def change_mac_address(interface, new_mac_address):
    """
    Change MAC Address of an interface

    :param interface: Interface to change its Mac Address
    :param new_mac_address: New MAC address
    """

    print(f"[+] Changing MAC address for {interface} to {new_mac_address}")

    # System calls to: bring down interface, change address, bring up interface
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac_address(interface):
    """
    Return the MAC address of the specified interface.
    Exit script if not able to read the MAC address
    """

    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("ascii")
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")
        sys.exit()


def main():
    options = get_arguments()

    current_mac_address = get_current_mac_address(options.interface)
    print(f"Current MAC = {str(current_mac_address)}")

    # Change the interface to have the new MAC address
    change_mac_address(options.interface, options.new_mac_address)

    # Check if the original MAC address has successfully changed
    current_mac_address = get_current_mac_address(options.interface)
    if current_mac_address == options.new_mac_address:
        print(f"[+] MAC address was successfully changed to {current_mac_address}")
    else:
        print(f"[-] MAC address did not get changed.")


if __name__ == "__main__":
    main()
