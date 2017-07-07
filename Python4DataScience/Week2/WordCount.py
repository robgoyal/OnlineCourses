# Name: WordCount.py
# Author: Robin Goyal
# Last-Modified: July 7, 2017
# Purpose: Return the 10 most common words in a text file ignoring
#          common words from stopwords file and punctuation such as (., ,).

import collections

# Store stopwords into list
with open('stopwords') as f:
    stopwords = f.read().splitlines()

file = open('98-0.txt')

# Dictionary to hold count of words
wordCount = {}

for line in file:

    # Strip line of punctuation
    line = "".join(c for c in line if c not in ('\n', '.', '"', ',', '“', '”'))
    
    # Split line into words
    words = line.split()

    for word in words:
        word = word.lower()

        # Ignore words existing in list of commond words
        if not(word in stopwords):

            # Increment count of word if word exists in Dictionary
            # Otherwise, add word to dictionary and set value to 0
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount[word] = 1

file.close()

# Use collections to return the top 10 common words
common_10 = collections.Counter(wordCount).most_common(10)
print(common_10)