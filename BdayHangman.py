import random
print("                             ~ WELCOME TO HANGMAN!! <3 ~")
again = True

def displayWord(word: str, display: str, guess: str) -> str:
    '''Returns the display to reflect the correctly guessed letter'''
    display = list(display)
    if word.count(guess) == 1:
        ind = word.index(guess)
        display[ind] = guess
    else:
        start = 0
        for i in range(word.count(guess)):
            ind = word[start:].index(guess)
            display[ind + start] = guess
            start = ind + 1
    display = "".join(display)
    return display

def drawHangman(lives: int) -> str:
    '''returns what the hangman should look like after a certain number of lives'''
    if lives == 7:
        return """
                           _________
                           |       |
                           |       
                           | 
                           |
                           |
                          ==="""
    elif lives == 6:
        return """
                   _________
                   |       |
                   |       O
                   | 
                   |
                   |
                  ==="""
    elif lives == 5:
        return """
                   _________
                   |       |
                   |       O
                   |       |
                   |
                   |
                  ==="""
    elif lives == 4:
        return """
                   _________
                   |       |
                   |       O
                   |      /|
                   |
                   |
                  ==="""
    elif lives == 3:
        return """
                   _________
                   |       |
                   |       O
                   |      /|\\
                   |
                   | 
                  ==="""
    elif lives == 2:
        return """
                   _________
                   |       |
                   |       O
                   |      /|\\
                   |       |
                   |
                  ==="""
    elif lives == 1:
        return """
                   _________
                   |       |
                   |       O
                   |      /|\\
                   |       |
                   |      /
                  ==="""
    elif lives == 0:
        return """
                   _________
                   |       |
                   |       O
                   |      /|\\
                   |       |
                   |      / \\
                  ==="""

def playAgain() -> bool:
    '''prompts the user to play again or not'''
    yesNo = input("\nWould you like to play again (y/n)? ").lower()
    return yesNo == "y"

def info() -> str:
    '''prints all info user needs to know before round'''
    print("\n" + hangman)
    print("\n\n" + display)
    print("\nYou have " + str(lives) + " lives left.")
    print("\nWrong Guessed letters = " + str(wrongGuesses))
    print("Right Guessed letters = " + str(rightGuesses))


while again:
    wordList = ["BEAUTIFUL", "INTELLIGENT", "KIND", "CARING", "FUNNY", "FILIPINO", "STRONG", "GANDA", ""]
    chosenWord = random.choice(wordList)
    wrongGuesses = []
    rightGuesses = []
    lives = 7
    display = "".join(["_" for _ in range(len(chosenWord))])
    hangman = drawHangman(lives)
    info()
    while lives > 0:
        guess = input("\nGuess a letter:\n").upper()
        if guess not in chosenWord:
            wrongGuesses.append(guess)
            lives -= 1
            hangman = drawHangman(lives)
            info()
            if lives == 0:
                print("\n" + "Oh no! You lost!! :( The word was: '" + chosenWord + "'. It's okay baby, get them next time!")
                again = playAgain()
                if not again:
                    print("Okay, thanks for playing. Goodbye, I love you!\nShutting down...")
                else:
                    print("YAY!! HAHAHA AGAIN!!!")
        else:
            rightGuesses.append(guess)
            display = displayWord(chosenWord, display, guess)
            info()
            if display == chosenWord:
                print("\nCongratulations!! You guessed the word!! It was '" + chosenWord + "'!\nGOOD JOB BABY :) <3    It Took you " + str(len(rightGuesses) + len(wrongGuesses)) + " guesses!")
                lives = 0
                again = playAgain()
                if not again:
                    print("\nOkay, thanks for playing. Goodbye, I love you!\nShutting down...")
                else:
                    print("\nYAY!! HAHAHA AGAIN!!!\n\n")
