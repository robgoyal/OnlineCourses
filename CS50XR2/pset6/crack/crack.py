# Name: crack.py
# Author: Robin Goyal
# Last-Modified: March 12, 2018
# Purpose: Implement a program which cracks passwords
#          encrypted by C's DES based crypt function


from crypt import crypt
import string
import sys


LETTERS = string.ascii_letters
SIZE = 52


def main():

    # Check if 2 arguments were passed
    if len(sys.argv) != 2:
        print("Usage: python crack.py hash")

    # First two characters of str_hash is the salt
    str_hash = sys.argv[1]
    salt = str_hash[:2]

    # Potential password length between 1 and 5 characters
    for i in range(1, 6):
        guess = [None] * i

        # 52 ** i possible values for guess of length i
        for j in range(SIZE ** i):
            temp = j

            # Construct guess for i letters
            for k in range(i):
                # last character of guess is remaining value in temp
                if k == i - 1:
                    guess[k] = LETTERS[temp % SIZE]

                else:
                    # Place value logic to determine letter for position k
                    place_value = SIZE ** (i - k - 1)
                    guess[k] = LETTERS[temp // place_value]
                    temp = temp % place_value

            # Check if hashed guess is equal to original hash
            guess = "".join(guess)
            if (crypt(guess, salt) == str_hash):
                print(guess)
                return


if __name__ == "__main__":
    main()