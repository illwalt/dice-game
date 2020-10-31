from random import randint
from time import sleep


# ------------Welcome screen--------------------------------
print("Welcome to Dice Game")
print("please add two players")

# ------------setting up players--------------------------------

# create players list to store player names
players = []

# loop to setup players loop will keep running till number of player is 2
while len(players) < 2:
    # get players name
    # set player name to title case so it matches name is list
    name = input("Enter player name: (type q to quit game) ").title()
    # allows user to quit out of game
    if name == "Quit" or name == "Q":
        print("You have ended the game")
        break
    # List with valid player names
    user_name = ["Tommy Egan", "Luke Skywalker", "Jasiah Adu-Southard"]
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

# ------------setting Dice Game--------------------------------

dice1 = randint(1, 6)
dice2 = randint(1, 6)
