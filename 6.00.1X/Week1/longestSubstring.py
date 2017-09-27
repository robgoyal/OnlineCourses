# Name: longestSubstring.py
# Author: Robin Goyal
# Last-Modified: September 27, 2017
# Purpose: Return the longest substring from a string input

# Hold indices for current sub string and max substring
maxSubStrIndices = [0, 0]
currSubStrIndices = [0, 0]


for i in range(len(s)-1):

    # Increment right most index if next char is greater than or equal to curr char
    if s[i+1] >= s[i]:
        currSubStrIndices[1] += 1
    else:
        # Update max substring indices to current indices if curr is greater than max
        if (currSubStrIndices[1] - currSubStrIndices[0]) > (maxSubStrIndices[1] - maxSubStrIndices[0]):
            maxSubStrIndices = list(currSubStrIndices)
            currSubStrIndices = [i+1, i+1]
        # Set curr sub string indices to next index
        else:
            currSubStrIndices = [i+1, i+1]

# Perform final check to verify if last set of substring wasnt the max
if (currSubStrIndices[1] - currSubStrIndices[0]) > (maxSubStrIndices[1] - maxSubStrIndices[0]):
    maxSubStrIndices = list(currSubStrIndices)

# Obtain the longest substring based off of max indices
substring = s[maxSubStrIndices[0]:maxSubStrIndices[1]+1]
print("Longest substring in alphabetical order is: {}".format(substring))