#This code generates a random integer between 1 and 100 and asks the user to guess the number.
#The user has an unlimited number of attempts to guess the number.
#After each guess, the code tells the user if their guess was too high or too low.
#The game ends when the user correctly guesses the number, and the code prints the number of attempts it took to guess the number.

import random

def guess_number():
    print("Welcome to the Guess the Number game!")
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if guess == secret_number:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
            break
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Too low. Try again.")

guess_number()
