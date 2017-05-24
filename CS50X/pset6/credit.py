# Name: Credit.py
# Author: Robin Goyal
# Last-Modified: May 24, 2017
# Purpose: Determine if a credit card is valid 
#          the type of credit card

import cs50

def main():
    
    # Get credit card number and split string into integer digits in array
    print("Credit Card Number: ", end = "")
    cardInput = str(cs50.get_int())
    cardNumber = [int(i) for i in cardInput]
    
    # result from luhns algorithm
    total = luhn(cardNumber)
        
    # Valid credit cards final digit is 0
    if (total % 10 == 0):
        
        # Visa condition
        if cardInput[0] == "4":
            print("VISA")
            
        # Amex condition
        elif cardInput[0:2] == "34" or cardInput[0:2] == "37":
            print("AMEX")
        
        # Mastercard condition
        elif cardInput[0:2] == "51" or cardInput[0:2] == "52" or cardInput[0:2] == "53" or \
            cardInput[0:2] == "54" or cardInput[0:2] == "55":
            print("MASTERCARD")
    else:
        print("INVALID")
    
    
# Luhns algorithm
def luhn(card):
    total = 0
    
    for i in range(len(card) - 2, -1, -2):
        temp = card[i] * 2
        if temp > 9:
            temp -= 9
        total += temp
        del card[i]
        
    total += sum(card)
    return total

if __name__ == "__main__":
    main()