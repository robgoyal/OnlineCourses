# Name: uniqueValues.py
# Author: Robin Goyal
# Last-Modified: January 10, 2018
# Purpose: Return a list of keys which appear exactly once in a dictionary


def uniqueValues(aDict):
    '''
    dict(int: int) -> list

    aDict: a dictionary
    returns: a sorted list

    Return a list of keys that map to unique aDict values, empty list if none

    Examples:
        ({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0} -> [1, 3, 8]
        ({1: 1, 2: 1, 3: 1}) -> []
    '''

    keys = []
    newDict = {}

    # Create dictionary which maps values to a list of keys
    # which held the same values in aDict
    for k, v in aDict.items():
        if v in newDict:
            newDict[v].append(k)

        else:
            newDict[v] = [k]

    # Create list by looking for values of newDict which contain one element
    for k, v in newDict.items():
        if len(newDict[k]) == 1:
            keys.append(v[0])

    return sorted(keys)


print(uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}))
print(uniqueValues({1: 1, 2: 1, 3: 1}))
