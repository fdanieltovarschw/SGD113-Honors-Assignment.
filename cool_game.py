"""
Cool_game.py
------------
A simple number‑guessing game demonstrating basic Python concepts:
- variables
- loops
- conditionals
- functions
- user input

This program was developed with the assistance of Microsoft Copilot,
which helped brainstorm the structure, logic, and documentation.
"""

import random

def intro():
    print("Welcome to Cool Game!")
    print("I'm thinking of a number between 1 and 20.")
    print("Try to guess it in as few attempts as possible.\n")

def get_guess():
    """Safely get a number from the user."""
    while True:
        guess = input("Enter your guess: ")
        if guess.isdigit():
            return int(guess)
        print("Please enter a valid number.")

def play_game():
    secret = random.randint(1, 20)
    attempts = 0

    while True:
        guess = get_guess()
        attempts += 1

        if guess < secret:
            print("Too low! Try again.\n")
        elif guess > secret:
            print("Too high! Try again.\n")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break

def main():
    intro()
    play_game()

    while True:
        again = input("\nPlay again? (y/n): ").lower()
        if again == "y":
            print()
            play_game()
        elif again == "n":
            print("Thanks for playing Cool Game!")
            break
        else:
            print("Please type 'y' or 'n'.")

if __name__ == "__main__":
    main()
