# Name: howMany.py
# Author: Robin Goyal
# Last-Modified: October 28, 2017
# Purpose: Return the number of values in dictionary

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''

    values = sum(map(len, aDict.values()))
    return values