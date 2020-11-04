from random import randint
from time import sleep
import sys
import operator


rounds = 0
score1 = 0
score2 = 0


# ------------Welcome screen--------------------------------
print("--------Welcome to Dice Game---------")
print("1. Please enter 'n' to add new player")
print("2. Please enter 'p' to play Dice Game")
print("3. Please enter 's' to display scores")
print("4. Please enter 'q' to quit game")

menu = input("\nPlease select option from menu: ").lower()
while menu not in ["n", "p", "s", "q"]:
    menu = input("\nPlease select option from menu: ").lower()

if menu == "q":
    print("You have ended the game")
    sys.exit()

if menu == "n":
    username = input("Please enter username: ")
    pword1 = input("Please enter password: ")
    pword2 = input("Please re-enter password: ")
    if pword1 == pword2:
        print("User account successfully created")
        file = open ( "users.txt", "a" )
        file.write("username: ")
        file.write(username)
        file.write(" ")
        file.write("password: ")
        file.write(pword2)
        file.write("\n")
        file.close()
        print("\nPlease select option from menu: ")
        menu = input("").lower()
    if pword1 != pword2:
        correct_pword = (pword1)
        while True:
            print("Passwords did noy match")
            pword = input("Enter password again: ")
            if pword == correct_pword:
                print("Correct password has been entered")
                f = open ("users.txt", "a+" )
                f.write("username: ")
                f.write(username)
                f.write(" ")
                f.write("password: ")
                f.write(correct_pword)
                f.write("\n")
                f.close()
                print("\nPlease select option from menu: ")
                menu = input("").lower()
            else:
                print('Incorrect password ')

# create players list to store player names
players = []
check_failed = True

while check_failed:
    print("Could player 1 enter their username and password")
    username1 = input("Please enter your username ")
    password = input("Please enter your password ")
    with open("users.txt","r") as player_file:
        for line in player_file:
            if (f"username: {username1} password: {password}") == line.strip():
                players.append(username1.title())
                print(f"Player #1 is {players[0]}")
                check_failed = False
                check_failed = True
                while check_failed:
                    print("Could player 2 enter their username and password")
                    username2 = input("Please enter your username ")
                    password = input("Please enter your password ")
                    with open("users.txt","r") as player_file:
                        for line in player_file:
                            if (f"username: {username2} password: {password}") == line.strip():
                                players.append(username2.title())
                                print(f"Player #2 is {players[1]}")
                                check_failed = False
                                sleep(2)
                                print("-------------------------------------------")
                                print("Dice Game Starting.......")
                                print("-------------------------------------------")
                                sleep(2)

# ------------Dice Game-------------------------------------
while rounds < 5:
    # player one
    print(f"\n--------{players[0].title()} Rolling Round #{rounds + 1}-----\n")
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
    score1 += total  # score1 = 100
    print(f"Player score is: {score1}")
    if score1 <= 0:
        print("-------------------------------------------")
        print(f"{players[0]} you have lost the game")
        print("-------------------------------------------")
        sys.exit()

    # player 2
    print(f"\n--------{players[1].title()} Rolling Round #{rounds + 1}-----\n")
    dice1 = randint(1, 6)
    print(f"Dice #1 this round is: {dice1}")
    sleep(2)
    dice2 = randint(1, 6)
    print(f"Dice #2 this round is: {dice2}")
    sleep(2)
    total = dice1 + dice2
    if dice1 == dice2:
        print("Adding 10 points for even total.")
        total += 10
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
    score2 += total  # score2 = 100
    print(f"Player score is: {score2}")
    if score2 <= 0:
        print("-------------------------------------------")
        print(f"{players[1]} you have lost the game")
        print("-------------------------------------------")
        sys.exit()
    rounds += 1

# player_scores = [[players[0], score1], [players[1], score2]]
print("\n")
print("-------------------------------------------")
print(f"Total score for player 1 - {players[0]} is", score1)
print("-------------------------------------------")
print(f"Total score for player 2 - {players[1]} is", score2)
print("-------------------------------------------")

# ------------Tie break-------------------------------------
no_win = True

while no_win:
    if score1 == score2:
    print("Drawn Game")
    print("Each player rolls one die again to see who scores the highest")

    tie_break = input("Press \"y\" to roll: ")
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
