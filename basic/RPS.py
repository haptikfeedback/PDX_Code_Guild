# Let's play a game "Rock, Paper, or Scisors"

import random

rps_list = ["Rock", "Paper", "Scissor"]
player_wins = 0
computer_wins = 0

print("\nLet's play a game!\nRock, Paper, or Scissors!\nBest of 3 wins\n")

while player_wins < 3 and computer_wins < 3:
    rps_random_list = random.choice(rps_list)
    challenge = input("Press:\n1 for Rock\n2 for Paper\n3 for Scissors.\n\n:")
    if str(challenge) == "1":
        if rps_random_list == "Rock":
            print("Tied, I threw " + rps_random_list)
        elif rps_random_list == "Paper":
            player_wins = player_wins + 1
            print("You win, I threw " + rps_random_list)
        else:
            computer_wins = computer_wins + 1
            print("You lose, I threw " + rps_random_list)
    if str(challenge) == "2":
        if rps_random_list == "Rock":
            player_wins = player_wins + 1
            print("You win, I threw " + rps_random_list)
        elif rps_random_list == "Paper":
            print("Tied, I threw " + rps_random_list)
        else:
            computer_wins = computer_wins + 1
            print("You lose, I threw " + rps_random_list)
    if str(challenge) == "3":
        if rps_random_list == "Rock":
            computer_wins = computer_wins + 1
            print("You lose, I threw " + rps_random_list)
        elif rps_random_list == "Paper":
            player_wins = player_wins + 1
            print("You win, I threw " + rps_random_list)
        else:
            print("Tied, I threw " + rps_random_list)

if player_wins == 3:
    print("You won!")
elif computer_wins == 3:
    print("You lose!")

print("Computer Score: " + str(computer_wins) + "    Player Score: " + str(player_wins))
