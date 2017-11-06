# Name: uniqueValues.py
# Author: Robin Goyal
# Last-Modified: November 1, 2017
# Purpose: Return all the keys with unique values

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    
    uniqueKeys = []

    # Temporary dictionary to hold occurrences of specific values
    tempDict = {}

    for key in aDict:
        if aDict[key] in tempDict:
            tempDict[aDict[key]][0] += 1
        else:
            tempDict[aDict[key]] = [1, key]

    for key in tempDict:

        # Keys with unique values
        if tempDict[key][0] == 1:
            aList.append(tempDict[key][1])

    return sorted(uniqueKeys)