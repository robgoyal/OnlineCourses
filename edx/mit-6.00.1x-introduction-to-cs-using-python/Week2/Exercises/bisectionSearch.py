# Name: bisectionSearchpy
# Author: Robin Goyal
# Last-Modified: October 1, 2017
# Purpose: Use bisectionSearch to determine square of number

epsilon = 0.01
square = 25
guess = square

while abs(guess ** 2 - square) >= epsilon:

    if (guess**2 > square):
        guess = guess / 2

    else:
        guess = (guess + 2*guess)/2

print(guess)