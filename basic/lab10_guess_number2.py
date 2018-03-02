import random

def playagain2():
    print("\n*********************************")
    print("*    You have entered a game     *")
    print("* Objective: I guess your number *")
    print("*       between 1 and 100        *")
    print("**********************************\n")
    cnumber = range(1, 100)
    cran_num = random.choice(cnumber)
    user_num = input("What is your number?")
    i = True
    while i == True:
        print("Is your number {}?".format(cran_num))
        computerguess = input("am I too high or too low?: ").lower()
        if computerguess == "too high":
            cnumber = range(1, cran_num)
            cran_num = random.choice(cnumber)
            print(user_num)
            print(cran_num)
        elif computerguess == "too low":
            cnumber = range(cran_num, 100)
            cran_num = random.choice(cnumber)
            print(user_num)
            print(cran_num)
        elif computerguess == "correct":
            print("I win!")
            i = False
