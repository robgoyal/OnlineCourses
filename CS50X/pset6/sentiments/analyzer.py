# Name: Analyzer.py
# Author: Robin Goyal
# Last-Modifed: May 28, 2017
# Purpose: Perform basic sentiment analysis on a string

import nltk

class Analyzer():
    """Implements sentiment analysis."""
    
    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        # list for positive and negative words
        self.positiveList = []
        self.negativeList = []
        
        # Open positive-words.txt file
        with open(positives) as lines:
            for line in lines:
                line = line.strip()
                
                # Check if line is a blank line or a commented line
                if (not line or line.startswith(";")):
                    continue
                else:
                    # Append word to positive list 
                    self.positiveList.append(line)
        
        # Open negative-words-txt file
        with open(negatives) as lines:
            for line in lines:
                line = line.strip()
                
                # Check if line is a blank line or a commented line
                if (not line or line.startswith(";")):
                    continue
                else:
                    # Append word to positive list
                    self.negativeList.append(line)
        
        # Create tokenizer object           
        self.tokenizer = nltk.tokenize.TweetTokenizer()
            
    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
            
        # Initialize score to 0
        score = 0
        
        # Pass text to tokenizer object and create list of tokens
        tokens = self.tokenizer.tokenize(text)
        
        # Iterate through tokens analyzing each token
        for token in tokens:
            # Increment score if token is positive word
            if token in self.positiveList:
                score += 1
            # Decrement token if token is negative word
            elif token in self.negativeList:
                score -= 1
                
        return score
