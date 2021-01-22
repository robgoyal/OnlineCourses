#!/usr/bin/env python
# Original MAC address: 08:00:27:23:ff:90

import optparse
import re
import subprocess


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
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
    :return:
    """

    print(f"[+] Changing MAC address for {interface} to {new_mac_address}")

    # System calls to: bring down interface, change address, bring up interface
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac_address(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("ascii")
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


def main():
    options = get_arguments()

    current_mac_address = get_current_mac_address(options.interface)
    print(f"Current MAC = {str(current_mac_address)}")

    change_mac_address(options.interface, options.new_mac_address)

    current_mac_address = get_current_mac_address(options.interface)
    if current_mac_address == options.new_mac_address:
        print(f"[+] MAC address was successfully changed to {current_mac_address}")
    else:
        print(f"[-] MAC address did not get changed.")


if __name__ == "__main__":
    main()
