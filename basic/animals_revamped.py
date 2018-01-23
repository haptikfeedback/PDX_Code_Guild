#favorite_color.py

favorite_color = ['blue']
guesses = 10

print("\nYou have to guess my favorite color. You have " + str(guesses) + " tries.\n")

while len(favorite_color) > 0:
    guess = input("What's your guess?\n\n:")
    guesses = guesses - 1
    if guess in favorite_color:
        favorite_color.remove(guess)
        print("Correct!")
    else:
        print("\nWrong, guess again! You have " + str(guesses) + " attempts.\n")
