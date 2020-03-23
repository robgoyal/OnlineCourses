# Name: countBob.py
# Author: Robin Goyal
# Last-Modified: September 26, 2017
# Purpose: Count the number of times bob occurs in string

countOfBob = 0

for i in range(len(s) - 2):

    # Look at the current 3 characters
    if s[i : i+3] == 'bob':
        countOfBob += 1

print("Number of times bob occurs is : {}".format(countOfBob))