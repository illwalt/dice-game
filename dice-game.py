from random import randint
from time import sleep
import sys


# ------------Welcome screen--------------------------------
print("Welcome to Dice Game")
print("please add two players")

# ------------setting up players----------------------------

# create players list to store player names
players = []

# loop to setup players loop will keep running till number of player is 2
while len(players) < 2:
    # get players name
    # set player name to title case so it matches name is list
    name = input("Enter player name: (type q to quit game) ")
    # allows user to quit out of game
    if name == "q" or name == "q":
        print("You have ended the game")
        sys.exit()
    # List with valid player names
    user_name = ["tommy", "luke", "jasiah"]
    #  check if names are valid and add to players list
    if name in user_name:
        players.append(name)
        print(f"{name} is a valid player")
        #  check if there are two player and print the players names
        if len(players) == 2:
            print(f"Player #1 is {players[0]}\nPlayer #2 is {players[1]}")
            print("Get ready to play Dice Game")
    #  tells you that the name you have enetered is not valid
    else:
        print(f"{name} is not a valid player try again.")

# ------------Dice Game-------------------------------------

# setting up the dice

rolls = 0
score1 = 0
score2 = 0
# player_scores = []

while rolls < 1:
    # player one
    print(f"\n--------{players[0].title()} Rolling Round #{rolls + 1}-----\n")
    dice1 = randint(1, 6)
    print(f"Dice #1 this round is: {dice1}")
    sleep(2)
    dice2 = randint(1, 6)
    print(f"Dice #2 this round is: {dice2}")
    sleep(2)
    total = dice1 + dice2
    if dice1 == dice2:
        print("Rolling dice again for double")
        dice3 = randint(1, 6)
        print(f"Extra roll total: {dice3}")
        total += dice3
    elif total % 2 == 0:
        total += 10
        print("Adding 10 points for even total.")
    else:
        total -= 5
        print("Subtracting 5 points for odd total.")
    print(f"Round total is: {total}")
    score1 = 100
    print(f"Player score is: {score1}")
    if score1 <= 0:
        print("-------------------------------------------")
        print(f"{players[0]} you have lost the game")
        print("-------------------------------------------")
        sys.exit()

    # player 2
    print(f"\n--------{players[1].title()} Rolling Round #{rolls + 1}-----\n")
    dice1 = randint(1, 6)
    print(f"Dice #1 this round is: {dice1}")
    sleep(2)
    dice2 = randint(1, 6)
    print(f"Dice #2 this round is: {dice2}")
    sleep(2)
    total = dice1 + dice2
    if dice1 == dice2:
        print("Rolling dice again for double")
        dice3 = randint(1, 6)
        print(f"Extra roll total: {dice3}")
        total += dice3
    elif total % 2 == 0:
        total += 10
        print("Adding 10 points for even total.")
    else:
        total -= 5
        print("Subtracting 5 points for odd total.")
    print(f"Round total is: {total}")
    score2 = 100
    print(f"Player score is: {score2}")
    if score2 <= 0:
        print("-------------------------------------------")
        print(f"{players[1]} you have lost the game")
        print("-------------------------------------------")
        sys.exit()
    rolls += 1

# player_scores = [[players[0], score1], [players[1], score2]]
print("\n")
print("-------------------------------------------")
print(f"Total score for player 1 - {players[0]} is", score1)
print("-------------------------------------------")
print(f"Total score for player 2 - {players[1]} is", score2)
print("-------------------------------------------")

# ------------Sudden Death-------------------------------------
no_win = "y"

if score1 == score2:
    print("Drawn Game")
    print("Each player rolls one die again to see who scores the highest")
# while no_win == "y"
    player1 = input("Press \"y\" to roll: ")
    print(player1)
    if player1 == "y":
        print("rolling......")
        sleep(2)
        dice_sd1 = randint(1, 6)
        print(f"this round is: {dice_sd1}")
        player1_score = dice_sd1
        print(f"{players[0]} has rolled {player1_score}")

    player2 = input("Press \"y\" to roll: ")
    print(player1)
    if player2 == "y":
        print("rolling......")
        sleep(2)
        dice_sd2 = randint(1, 6)
        print(f"this round is: {dice_sd2}")
        player2_score = dice_sd2
        print(f"{players[1]} has rolled {player2_score}")

elif score1 > score2:
    print(f"{players[0]} is the winner of this game.")
    print("-------------------------------------------")
else:
    print(f"{players[1]} is the winner of this game.")
    print("-------------------------------------------")
