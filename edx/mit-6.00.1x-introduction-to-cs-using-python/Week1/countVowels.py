# Name: countVowels.py
# Author: Robin Goyal
# Last-Modified: September 26, 2017
# Purpose: Count the number of vowels in a string

numOfVowels = 0

for i in s:
    if i in "aeiou":
        numOfVowels += 1

print("Number of vowels: {}".format(numOfVowels))