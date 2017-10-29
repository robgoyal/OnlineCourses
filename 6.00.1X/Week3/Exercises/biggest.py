# Name: biggest.py
# Author: Robin Goyal
# Last-Modified: October 28, 2017
# Purpose: Return the key with the largest number of values

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''

    # Initialize variables
    max_value_len = 0
    max_key = None
    
    # Find key with max number of values values
    for key in aDict:
        if len(aDict[key]) >= max_value_len:
            max_key = key
    
    return max_key