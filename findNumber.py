""" Development Exercises – L1
Create a program invoked in the command line. It generatesa random number between 1 and 30
(including 1 and 30). Ask the user to guess the number, then tell them whether they guessed
too low, too high, or exactly right. Keep the game going until the user types “exit” or
find the numberKeep track of how many guesses the user has taken, and when the game ends,
print themouton console and in a file named GuessingSteps.txt

:authors: - Hugo Rodríguez
"""

import random
from datetime import datetime

numberToGuess = int(random.random() * 100) % 30 + 1

logFile = open('GuessingSteps.txt', 'a+')
logFile.write(f"\n{datetime.today().strftime('%Y-%m-%d-%H:%M:%S')} Run\n")

keepGuessing = True
while keepGuessing:
    guessInput = input("Guess number: ")

    if not guessInput.isdigit():
        if 'exit' == guessInput:
            keepGuessing = False
            logFile.write("exit\n")
        else:
            print(f"Invalid number or option given: {guessInput}")
        continue

    guess = int(guessInput)
    logFile.write(guessInput + ': ')

    if guess < numberToGuess:
        print('Too low')
        logFile.write('too low\n')
    elif guess > numberToGuess:
        print('Too high')
        logFile.write('too high\n')
    elif guess == numberToGuess:
        print('Exactly right')
        logFile.write('exactly right\n')
        keepGuessing = False

logFile.close()