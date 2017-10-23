import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    secretWordlist=[]
    for i in range(len(secretWord)):
        secretWordlist.append(secretWord[i])
    temp=[]
    for i in range(len(secretWordlist)):
        j=0
        while j < len(lettersGuessed):
            if secretWordlist[i]==lettersGuessed[j]:
                temp.append(secretWordlist[i])
                break
            else:
                j=j+1
    if temp == secretWordlist:
        return True
    else:
        return False




def getGuessedWord(secretWord, lettersGuessed):
    result=''
    for e in secretWord:
        if  e in lettersGuessed:
            result=result+e
        else:
            result=result+'_ '
    return result

def getAvailableLetters(lettersGuessed):
    import string 
    char=string.ascii_lowercase
    result=''
    for e in char:
        if e in lettersGuessed:
            continue
        else:
            result=result+e
    return result    

def hangman(secretWord):
    print 'Welcome to the game,Hangman!'
    print 'I am thinking of a word that is %d letters long'%len(secretWord)
    print '-----------'
    lettersGuessed=[]
    mistakesMade=0
    availableLetters='abcdefghijklmnopqrstuvwxyz'
    flag='w'
    repeat=False
    while True:
        print 'You have %d guesses left'%(8-mistakesMade)
        print 'Available letters: '+availableLetters
        letter=raw_input('Please guess a letter: ')
        lettersguessed=letter.lower()
        if lettersguessed in lettersGuessed:
            repeat=True
        else:
            lettersGuessed.append(lettersguessed)
        availableLetters=getAvailableLetters(lettersGuessed)
        if lettersguessed not in secretWord or repeat:
            print 'Oops!That letter is not in my world: %s'%getGuessedWord(secretWord, lettersGuessed)
            print '-----------'
            if mistakesMade<7:
                mistakesMade=mistakesMade+1
                continue
            elif mistakesMade==7:
                flag='f'
                break
        else:
            print 'Good guess:%s'%getGuessedWord(secretWord, lettersGuessed)
            print '-----------'
            if isWordGuessed(secretWord, lettersGuessed):
                flag='s'
                break
            else:
                continue

    if flag == 's':
        print 'Congratulations, you won!'
    elif flag == 'f':
        print 'Sorry, you ran out of guesses. The word was else. '



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
