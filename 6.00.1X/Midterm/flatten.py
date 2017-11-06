# Name: flatten.py
# Author: Robin Goyal
# Last-Modified: November 1, 2017
# Purpose: Flatten all nested lists into a single list

def flatten(aList):

    temp = []
    for elem in aList:

        # Recursively flatten nested list
        if type(elem) == list:
            temp.extend(flatten(elem))
        else:
            temp.append(elem)

    return temp


print(flatten([1, 2, [3, [4, 5]], 4, 6]))