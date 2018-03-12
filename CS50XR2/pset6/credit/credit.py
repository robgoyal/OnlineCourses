# Name: credit.py
# Author: Robin Goyal
# Last-Modified: March 12, 2018
# Purpose: Determine whether a credit card number is valid


import cs50


def main():

    # Get card number
    card_number = cs50.get_int("Number: ")

    # Create array of digits from card number
    card_digits = [int(digit) for digit in reversed(str(card_number))]

    # Calculate sum as specified in Luhn's algorithm
    luhn_sum = 0

    for i in range(len(card_digits)):

        # Sum the individual digits in 2 * digit for every other digit
        if i % 2 == 1:
            luhn_sum += sum(int(digit) for digit in str(2 * card_digits[i]))
        else:
            luhn_sum += card_digits[i]

    print(check_luhn_sum(reversed(card_digits), luhn_sum))


def check_luhn_sum(arr, luhn):
    """
    (list, int) -> str

    Return a string indicating the type of the card
    after checking if the luhn sum is valid and arr
    checking the specific card values
    """

    if luhn % 10 != 0:
        return "INVALID"

    # Cards beginning with 34 or 37 are AMEX
    if arr[0] == 3 and (arr[1] in (4, 7)):
        card_type = "AMEX"

    # Cards beginning with 4 are VISA
    elif arr[0] == 4:
        card_type = "VISA"

    # Remaining cards are mastercard
    else:
        card_type = "MASTERCARD"

    return card_type


if __name__ == "__main__":
    main()