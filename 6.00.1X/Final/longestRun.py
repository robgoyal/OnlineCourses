# Write a function called longestRun, which takes as a parameter a list of integers named L (assume L is not empty). This function returns the length of the longest run of monotonically increasing numbers occurring in L. A run of monotonically increasing numbers means that a number at position k+1 in the sequence is either greater than or equal to the number at position k in the sequence.

# For example, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] then your function should return the value 5 because the longest run of monotonically increasing integers in L is [3, 4, 5, 7, 7].

# Name: longestRun.py
# Author: Robin Goyal
# Last-Modified: January 10, 2018
# Purpose: Return the max number of increasing elements in a sequence


def longestRun(L):
    '''
    list -> int

    Return an integer representing the number of maximally increasing
    values in a list.

    Examples:
        [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] -> 5
        [1, 2, 0, 4, 5] -> 3
        [3] -> 1
    '''

    max_seq_len = 0
    start, end = 0, 0

    for i in range(len(L) - 1):
        if L[i + 1] >= L[i]:
            end += 1

        else:
            diff = end - start + 1
            max_seq_len = max(diff, max_seq_len)
            start, end = i + 1, i + 1

    # Check if final element of list was part of largest increasing sequence
    if end != start:
        max_seq_len = max(end - start + 1, max_seq_len)
    elif len(L) == 1:
        return 1

    return max_seq_len


print(longestRun([10, 4, 6, 8, 3, 4, 5, 7, 7, 2]))
print(longestRun([10, 5, 2, 2]))
print(longestRun([0]))
