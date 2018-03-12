# Name: mario.py
# Author: Robin Goyal
# Last-Modified: March 12, 2018
# Purpose: Print Mario's double pyramids with a specified height


import cs50


def main():

    # Get height from user between 0 and 23
    height = cs50.get_int("Height: ")

    while not 0 < height < 23:
        height = cs50.get_int("Height: ")

    for i in range(height):
        spaces = " " * (height - i - 1)
        blocks = "#" * (i + 1)

        row = f"{spaces}{blocks}  {blocks}"
        print(row)


if __name__ == "__main__":
    main()