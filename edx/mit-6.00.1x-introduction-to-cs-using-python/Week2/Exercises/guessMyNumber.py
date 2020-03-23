# Name: guessMyNumber.py
# Author: Robin Goyal
# Last-Modified: October 1, 2017
# Purpose: Use bisection search to guess a number

low = 0
high = 100
mid = (high + low) // 2

msg = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. " 

print("Please think of a number between 0 and 100!")

while (True):
    print("Is your secret number {}?".format(mid))
    value = input(msg)
    
    # User input to indicate high low or correct
    if value == 'h':
        high = mid
    elif value == 'l':
        low = mid
    elif value == 'c':
        print("Game over, your secret number was: {}".format(mid))
        break
    else:
        print("Sorry, I did not understand your input")

    # Update middle value to reflect new range
    mid = (low + high)//2