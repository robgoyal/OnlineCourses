# Name: Veigenere.py
# Author: Robin Goyal
# Last-Modified: May 24, 2017
# Purpose: Encrypt plaintext by using a key and the veigenere cipher

import cs50
import sys

def main():
    
    # Verify only 2 command line arguments and key is alphabetic
    if not(sys.argv[1].isalpha()) or len(sys.argv) != 2:
        print("Usage: ./vigenere k")
        exit(1)
     
    # Lowercase key   
    key = sys.argv[1].lower()
    
    print("Plaintext: ", end ="")
    plaintext = cs50.get_string()
    print("Ciphertext: ", end = "")
    
    encrypt(plaintext, key)

# Encrypt function prints individual encrypted keys to the console
def encrypt(plaintext, key):
    
    keyIndex = -1
    for i in plaintext:
        
        # Check if current character is alphabetic
        if i.isalpha():
            keyIndex += 1
            
            # Different algorithm based off of uppercase or lowercase
            if i.isupper():
                char = (((ord(i) - ord('A')) + ord(key[keyIndex % len(key)]) - ord('a'))) % 26 + ord('A')
                print(chr(char), end = "")
            
            elif i.islower():
                char = (((ord(i) - ord('a')) + ord(key[keyIndex % len(key)]) - ord('a'))) % 26 + ord('a')
                print(chr(char), end = "")
        
        # Print character if not alphabetic
        else:
            print(i, end="")
            continue
    print()
    return

if __name__ == "__main__":
    main()