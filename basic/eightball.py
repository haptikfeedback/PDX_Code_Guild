# a magic eightball in the terminal
import random

def wiseEightball():
    question = input("What would you like to ask the all powerful EIGHTBALL!!?\n>>:")
    answer_list = ("Try again", "It doesn't look good", "Duck", "Absolutely", "Does Trump have hair!?", " Neva"
                   , "Stop bothering me", "Ok", "You tell me")
    print("The Magic Eightball returns\n\t" + random.choice(answer_list))
    answer = input("Would you like to play again?: ".lower())

    while True:
        if answer == 'yes':
            wiseEightball()
        elif answer == 'no':
            quit()


print(wiseEightball())
