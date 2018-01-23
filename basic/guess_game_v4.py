#Guessing Game

import random

messages = 

numbers = range(1,10)
user_continue = ['']
attempts = 0

print("\n\nLet's play a game!\n")

continue_game = True
computer_guess = random.choice(numbers)

while continue_game == True:
    user_guess = int(input("Guess a number between 1 and 10.\n:"))
    if user_guess == computer_guess:
         print("That is correct! I guessed " + str(computer_guess) + ".\n")
         user_continue = input("would you like to play again?\n:")
         if user_continue == ('yes' or 'Yes'):
            continue_game = True
            computer_guess = random.choice(numbers)
         else:
            continue_game = False
    elif user_guess < computer_guess:
        attempts = attempts + 1


    elif user_guess > computer_guess:
        attempts = attempts + 1
 