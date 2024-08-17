# -*- coding: utf-8 -*-
"""
This code is about guessing number game
Created on Fri Aug  9 14:09:11 2024

@author: Ajaykrishna28
"""

import random

 # Generate a random number between 1 and 100
random_number = random.randint(1, 100)
attempts = 0

print(" Welcome to the Number Guessing Game! ")
print(" I have generated a random number between 1 and 100. ")
print(" Can you guess what it is? ")

while True:
    try:
        guess = int(input("\n Enter your guess: "))
        attempts += 1

        if random_number - guess > 5:
            print(" You are too below! Try again.")
        elif guess < random_number:
            print(" You are just below the number!! Try once again. ")
        elif guess - random_number > 5:
            print(" You are too above! Try again ")
        elif guess > random_number:
            print(" You are just above the number!! Try once again. ")
        else:
            print(f" Congratulations! You've guessed the number correctly in {attempts} attempts. ")
            break
    except ValueError:
        print(" Invalid input. Please enter a number between 1 and 100. ")
