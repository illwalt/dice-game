from random import randint
from time import sleep
from datetime import datetime
import sys
# import operator

rounds = 0
score1 = 0
score2 = 0
score1_tb = 0
score2_tb = 0
users = {"test": "1234", "tommy": "1234", "luke": "1234" }
date = datetime.now()
game_date = (date.strftime("%d-%b-%Y %H:%M:%S"))


# ------------Welcome screen--------------------------------
print("\n--------Welcome to Dice Game---------")
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
        users[username] = pword2
        input("\nPress 'enter' to play Dice Game")
        menu = input("").lower()
    if pword1 != pword2:
        correct_pword = (pword1)
        while True:
            print("Passwords did noy match")
            pword2 = input("Enter password again: ")
            if pword2 == correct_pword:
                print("Correct password has been entered")
                print("User account successfully created")
                users[username] = pword2
                input("\nPress 'enter' to play Dice Game")
            else:
                print('Incorrect password ')

check_failed = True
while check_failed:
    print("Could player 1 enter their username and password")
    username1 = input("Please enter your username ")
    pword = input("Please enter your password ")
    for u,p in users.items():
        if u == username1 and p == pword:
            username1 = username1.title()
            print(f"Player #1 is {username1}")
            check_failed = False
            check_failed = True
            while check_failed:
                print("Could player 2 enter their username and password")
                username2 = input("Please enter your username ")
                pword = input("Please enter your password ")
                for u,p in users.items():
                    if u == username2 and p == pword:
                        username2 = username2.title()
                        print(f"Player #2 is {username2}")
                        check_failed = False
                        sleep(2)
                        print("-------------------------------------------")
                        print("Dice Game Starting.......")
                        print("-------------------------------------------")
                        sleep(2)

# ------------Dice Game-------------------------------------

while rounds < 5:
    # player one
    input(f"\n{username1} hit 'enter' roll dice")
    print("\nrolling......")
    print(f"\n--------{username1} Rolling Round #{rounds + 1}-----\n")
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
    # print(score1)
    # score1 += total
    score1 = 100
    print(f"Player score is: {score1}")
    print("-------------------------------------------")
    if score1 <= 0:
        print("-------------------------------------------")
        print(f"{username1} you have lost the game")
        print("-------------------------------------------")
        sys.exit()



    # player 2
    input(f"\n{username2} hit 'enter' roll dice")
    print("\nrolling......")
    print(f"\n--------{username2} Rolling Round #{rounds + 1}-----\n")
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
    # print(score2)
    # score2 += total
    score2 = 100
    print(f"Player score is: {score2}")
    print("-------------------------------------------")
    if score2 <= 0:
        print("-------------------------------------------")
        print(f"{username2} you have lost the game")
        print("-------------------------------------------")
        sys.exit()
    rounds += 1


print("\n")
print("-------------------------------------------")
print(f"Total score for player 1 - {username1} is", score1)
print("-------------------------------------------")
print(f"Total score for player 2 - {username2} is", score2)
print("-------------------------------------------")

# ------------Tie break-------------------------------------

if score1 == score2:
    print("Game Drawn")
    print("-------------------------------------------")
    print("\n************************TIE BREAK****************************")
    print("Each player rolls one die again to see who scores the highest")
    sleep(2)
    no_win = True
    while no_win:
        input(f"\n{username2} hit 'enter' roll dice")
        print("\nrolling......")
        sleep(2)
        dice_tb1 = randint(1, 6)
        print(f"\n--------{username1} Tie Break--------\n")
        score1_tb = dice_tb1
        print(f"{username1} rolled: {score1_tb}")
        if score1_tb % 2 == 0:
            score1_tb += 10
            print("Adding 10 points for even total.")
            print(f"{username1} score is: {score1_tb}")
        else:
            score1_tb -= 5
            print("Subtracting 5 points for odd total.")
            print(f"{username1} score is: {score1_tb}")
        if score1_tb <= 0:
            print("-------------------------------------------")
            print(f"{username1} you have lost the game")
            print("-------------------------------------------")
            file = open("scores.txt","a")
            file.write(username2)
            file.write(" scored ")
            file.write(str(score2))
            file.write(" points ")
            file.write("on ")
            file.write(game_date)
            file.write(" after a tie break")
            file.write("\n")
            file.close()
            sys.exit()

        input(f"\n{username2} hit 'enter' roll dice")
        print("\nrolling......")
        sleep(2)
        dice_tb2 = randint(1, 6)
        print(f"\n--------{username2} Tie Break--------\n")
        score2_tb = dice_tb2
        print(f"{username2} rolled: {score2_tb}")
        if score2_tb % 2 == 0:
            score2_tb += 10
            print("Adding 10 points for even total.")
            print(f"{username2} score is: {score2_tb}")
        else:
            score2_tb -= 5
            print("Subtracting 5 points for odd total.")
            print(f"{username2} score is: {score2_tb}")
        if score2_tb <= 0:
            print("-------------------------------------------")
            print(f"{username2} you have lost the game")
            print("-------------------------------------------")
            file = open("scores.txt","a")
            file.write(username1)
            file.write(" scored ")
            file.write(str(score2))
            file.write(" points ")
            file.write("on ")
            file.write(game_date)
            file.write(" after a tie break")
            file.write("\n")
            file.close()
            sys.exit()
        if score1_tb == score2_tb:
            print("-------------------------------------------")
            print("Still no winner you will have to roll again")
            print("-------------------------------------------")
        elif score1_tb > score2_tb:
            no_win = False
            print("-------------------------------------------")
            print(f"{username1} is the winner of this game.")
            print("-------------------------------------------")
            file = open("scores.txt","a")
            file.write(username1)
            file.write(" scored ")
            file.write(str(score1))
            file.write(" points ")
            file.write("on ")
            file.write(game_date)
            file.write(" after a tie break")
            file.write("\n")
            file.close()
        else:
            no_win = False
            print("-------------------------------------------")
            print(f"{username2} is the winner of this game.")
            print("-------------------------------------------")
            file = open("scores.txt","a")
            file.write(username2)
            file.write(" scored ")
            file.write(str(score2))
            file.write(" points ")
            file.write("on ")
            file.write(game_date)
            file.write(" after a tie break")
            file.write("\n")
            file.close()

elif score1 > score2:
    print(f"{username1} is the winner of this game.")
    print("-------------------------------------------")
    file = open("scores.txt","a")
    file.write(username1)
    file.write(" scored ")
    file.write(str(score1))
    file.write(" points ")
    file.write("on ")
    file.write(game_date)
    file.write("\n")
    file.close()
else:
    print(f"{username2} is the winner of this game.")
    print("-------------------------------------------")
    file = open("scores.txt","a")
    file.write(username2)
    file.write(" scored ")
    file.write(str(score2))
    file.write(" points ")
    file.write("on ")
    file.write(game_date)
    file.write("\n")
    file.close()
