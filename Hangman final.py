#Noah Gaviña
#2.25.19
#Hangman
import random
name = input("Hello, what is your name?:")
if name == "whiteface":
    exit()
print("Ok " + name + " let's play hangman.")

HANGMANPICS = ['''

      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      0   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      0   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      0   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      0   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      0   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      0   |
     /|\  |
     / \  |
          |
    =========''']
words = 'lumbago doom wolfenstein arthur morgan uncle john marston depression anxiety autism noah gavina sebastian pamela manuel chainsaw fist pistol shotgun super chaingun rocket launcher whiteface persona shadow self facade mask cat bear android fool magician priestess empress emperor hierophant lovers chariot justice hermit fortune strength hangman death temperance devil tower star moon sun judgement world psyche'.split()

def getRandomWord(wordList):
    #This gets a random word from the list.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
            print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): #This will replace the blanks with the letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: #Shows the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # This returns the letter entered and makes sure it is only a single letter.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose another.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER, not a number or other character.')
        else:
            return guess
def playAgain():
    #True if player wants to play again otherwise False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
def wordBank():
    #True if the player wants to see the word bank
    print('Would you like a word bank before you start? (yes or no)')
    return input().lower().startswith('y')
if wordBank():
    print('The words are as follows:')
    print('lumbago doom wolfenstein arthur morgan uncle john marston depression anxiety autism noah gavina sebastian pamela manuel chainsaw fist pistol shotgun super chaingun rocket launcher whiteface persona shadow self facade mask cat bear android fool magician priestess empress emperor hierophant lovers chariot justice hermit fortune strength hangman death temperance devil tower star moon sun judgement world psyche')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    #Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! the secret word was "' +secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        #Check if the player guessed too much and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    #Ask the player if they want to play again (only if the game is done).
    if gameIsDone:
        if wordBank():
            print('the words are as follows:')
            print('lumbago doom wolfenstein arthur morgan uncle john marston depression anxiety autism noah gavina sebastian pamela manuel chainsaw fist pistol shotgun super chaingun rocket launcher whiteface persona shadow self facade mask cat bear android fool magician priestess empress emperor hierophant lovers chariot justice hermit fortune strength hangman death temperance devil tower star moon sun judgement world psyche')
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
input("Goodbye " + name + "!")
