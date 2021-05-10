""" Development Exercises – L1
Create a program invoked in the command line. It generates a random number
between 1 and 30(including 1 and 30). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.
Keep the game going until the user types “exit” or find the numberKeep
track of how many guesses the user has taken, and when the game ends, print
themouton console and in a file named GuessingSteps.txt

:authors: - Hugo Rodríguez
"""

import random
from datetime import datetime

numberToGuess = int(random.random() * 100) % 30 + 1

log_file = open('GuessingSteps.txt', 'a+')
log_file.write(f"\n{datetime.today().strftime('%Y-%m-%d-%H:%M:%S')} Run\n")

keep_guessing = True
while keep_guessing:
    guess_input = input("Guess number: ")

    if not guess_input.isdigit():
        if guess_input == 'exit':
            keep_guessing = False
            log_file.write("exit\n")
        else:
            print(f"Invalid number or option given: {guess_input}")
        continue

    guess = int(guess_input)
    log_file.write(guess_input + ': ')

    if guess < numberToGuess:
        print('Too low')
        log_file.write('too low\n')
    elif guess > numberToGuess:
        print('Too high')
        log_file.write('too high\n')
    elif guess == numberToGuess:
        print('Exactly right')
        log_file.write('exactly right\n')
        keep_guessing = False

log_file.close()
