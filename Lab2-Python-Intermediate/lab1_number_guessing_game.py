"""
Lab Exercise 1: Number guessing game.
The computer picks a random number and the user has to guess it
within a limited number of attempts.
"""

import random


def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("---- Number Guessing Game ----")
    print(f"Guess a number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break
    else:
        print(f"Out of attempts! The number was {number_to_guess}.")


if __name__ == "__main__":
    number_guessing_game()
