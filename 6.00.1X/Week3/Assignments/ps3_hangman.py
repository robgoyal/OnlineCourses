# Name: ps3_hangman.py
# Author: Robin Goyal, MIT
# Last-Modified: October 29, 2017
# Purpose: Provide an interactive game of hangman allowing 8 wrong guesses
# Note: The helper functions loadWords and chooseWord were written by MIT staff

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    for letter in secretWord:

        # Return false if letter has not been guessed
        if letter not in lettersGuessed:
            return False

    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    # Initialize guess
    guess = ''

    for letter in secretWord:

        # Append letter if letter has been guessed
        if letter in lettersGuessed:
            guess += letter

        # Append blank if letter has not been guessed
        else:
            guess += '_ '

    return guess


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    # Create list of all characters in alphabet
    alphabet = list(map(chr, range(97, 123)))
    
    # Create string of letters not guessed 
    lettersNotGuessed = [letter for letter in alphabet if letter not in lettersGuessed]
    return "".join(lettersNotGuessed)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    # Initialize game variables
    guesses = 8
    guessed = False
    lettersGuessed = []

    # Introductory print statements
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long".format(len(secretWord)))
    print("------------")

    # Loop until all guesses have been used or correct word has been guessed
    while (guesses > 0 and not(guessed)):

        # Round start print statements
        print("You have {} guesses left.".format(guesses))
        print("Available letters: {}".format(getAvailableLetters(lettersGuessed)))

        # Input for letter guess
        letterGuess = input("Please guess a letter: ").lower()

        # Letter has already been guessed
        if letterGuess in lettersGuessed:
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            print("Oops! You've already guessed that letter: {}".format(guessedWord))

        # Letter in the secret word
        elif letterGuess in secretWord:
            lettersGuessed.append(letterGuess)
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            print("Good guess: {}".format(guessedWord))

        # Letter not in the word or not guessed
        else:
            lettersGuessed.append(letterGuess)
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            print("Oops! That letter is not in my word: {}".format(guessedWord))
            guesses -= 1

        print("------------")

        # Check if word has been guessed
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won")
            guessed = True

    # Word was not guessed with 8 guesses
    if not(guessed):
        print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)