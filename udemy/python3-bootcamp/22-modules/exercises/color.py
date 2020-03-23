# Name: color.py
# Author: Robin Goyal
# Last-Modified: March 8, 2019

import pyfiglet
import termcolor


def prettify(msg, color):
    """prettify(str, str)

    Display msg as ascii start in provided color.
    If not a valid color, default color is blue.

    :param msg: text to display
    :param color: color to display text in
    :return: formatted string information
    """

    art_msg = pyfiglet.Figlet().renderText(msg)
    if color not in termcolor.COLORS:
        color = "blue"

    return termcolor.colored(art_msg, color)


def main():
    msg = input("What message do you want to print? ")
    color = input("What color? ")

    print(prettify(msg, color))


if __name__ == "__main__":
    main()
