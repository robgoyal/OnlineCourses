# Name: oddTuples.py
# Author: Robin Goyal
# Last-Modified: October 28, 2017
# Purpose: Create new tuple with even indices of original tuple

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''

    oddTuple = ()
    
    for i in range(len(aTup)):

        # Concatenate to new tuple if even index
        if i % 2 == 0:
            oddTuple += (aTup[i], )
    return oddTuple