# Hangman game
#

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
    print("  ", len(wordlist), "words loaded.")
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
    # FILL IN YOUR CODE HERE...
    
    secret_word = list(secretWord)
    for i in secret_word:
        if i not in lettersGuessed:
            return False
    return True
            



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    new = ["_ " for i in secretWord]
    secret_word = list(secretWord)
    
    for i in secretWord:
        if i in lettersGuessed:
            new[secret_word.index(i)] = i
            secret_word[secret_word.index(i)] = '*'
            
        else:
            pass
    return "".join(new)




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    l = list('abcdefghijklmnopqrstuvwxyz')
    for i in lettersGuessed:
        if i in l:
            l.remove(i)
    return "".join(l)

    

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
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " +  str(len(secretWord)) + " letters long.")
    total_guess = 8
    lettersGuessed = []
    
    for i in range(total_guess):
        print("---------------------------")
        print("You have " + str(total_guess) + " guesses left")
        print("Available letters :" + getAvailableLetters(lettersGuessed))
        guess_letter = input("Please guess a letter : " )
        guess_letter = guess_letter.lower()
        lettersGuessed.append(guess_letter)
        
        
        
        if (isWordGuessed(secretWord, lettersGuessed)== True):
            print ("Good guess:" + getGuessedWord(secretWord, lettersGuessed))
            total_guess = total_guess - 1
            
            if ( "_" not in getGuessedWord(secretWord, lettersGuessed)):
                print("-------------------------------------")
                print("Congratulations, you won!")
                break
            
            
        
        elif (isWordGuessed(secretWord, lettersGuessed)== False):
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            total_guess = total_guess - 1
        
        
        elif (guess_letter in lettersGuessed = []):
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            
            
    
    
    if (total_guess == 0):
        print("-------------------------------------")
        print("Sorry, you ran out of guesses. The word was : " + secretWord)
        
        







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
