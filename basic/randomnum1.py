# Guess the Number (Player Edition)
from guess_the_num import playagain
from guess_the_num2 import playagain2

while True:
    playagain2()
    q = input("Would you like to play again?: ").lower()
    if q == "yes":
        pass
    elif q == "no":
        print("Thank you")
        break