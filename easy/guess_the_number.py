"""Guess the number."""

import random

secret_number = random.randint(1, 100)
ATTEMPTS = 0

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        user_guess = int(input("Enter your guess: "))
        ATTEMPTS += 1

        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(
                f"Congratulations! You guessed the number {secret_number} "
                f"in {ATTEMPTS} attempts."
            )
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")
