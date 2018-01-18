import random

def playagain():
    print("\n******************************")
    print("*  You have entered a game   *")
    print("* Objective: guess my number *")
    print("*    between 1 and 100       *")
    print("******************************\n")
    # user_input = input("Enter Guess: ")
    cnumber = range(1, 100)
    cran_num = random.choice(cnumber)
    i = True
    while i == True:
        try:
            user_input = int(input("What number do you think I guessed?: "))
        except ValueError:
            print('I forgot to mention, please use a numerical value')   
            continue 
        print("Computer Chose: {}".format(cran_num))
        if user_input < cran_num:
            print("Your guess is too low.")
        elif user_input > cran_num:
            print("Your guess is toooooo high")
        else:
            print("That is correct! I guessed {}".format(cran_num))
            i = False

    print("Computer Chose: {}".format(cran_num))