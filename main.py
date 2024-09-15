from art import logo
from random import randint


def set_initial_attempts():
    """Set the initial number of attempts at the start of the game"""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()  # User's difficulty choice
    # Change the number of attempts based on the chosen difficulty
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5


print(logo)
print("Welcome to the game Guess the number!\nI am thinking of a number between 1 and 100.")
answer = randint(1, 100)  # Generate a random number (the answer)
attempts = set_initial_attempts()  # Set the number of attempts based on a difficulty

while attempts > 0:  # Play the game until the number of attempts runs out
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Guess a number: "))  # User's guess

    if guess == answer:
        print(f"You guessed right! The right answer was {answer}! :)")
        break  # Exit the loop if the user guessed correctly
    elif guess < answer:
        print("Too low!\nGuess again!")
    else:
        print("Too high!\nGuess again!")

    attempts -= 1 # Lower the number of the attempts if the user guessed incorrectly

if attempts == 0:  # If the user runs out of attempts
    print("You ran out of attempts! You lost! :(")
