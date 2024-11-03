# Create a number guessing game program that:

# Generates a random number between 1 and 100.

# Asks the user to guess the number.

# Provides feedback:

# If the guess is too low, output "Too low, try again."
# If the guess is too high, output "Too high, try again."
# Continues prompting the user until they guess the correct number.

# Counts the number of attempts and displays it when the user guesses correctly.

import random

rand_num = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if guess < rand_num:
        print("Too low, try again")
    elif guess > rand_num:
        print("Too high, try again")
    else:
        print(f"You guessed the number in {attempts} attempts!")    
        break




