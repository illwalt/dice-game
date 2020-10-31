from random import randint
from time import sleep
import time
import sys
import random
import operator

total_score2 = 0
total_score1 = 0
rounds = 0
playerOnePoints = 0
playerTwoPoints = 0
print("*****************Welcome To The DICE Game*******************")
print("Please enter 'n' if you are a new user and 'e' if you are a exsiting user and enter 's' to display scores")
ens=input("")
while ens != ("e") and ens != ("n") and ens != ("s"): # if anything else but these characters are entered it will loop until it is correct
    print("Please enter 'n' if you are a new user and 'e' if you are a exsiting user and enter 's' to display scores")
    ens = input()
if ens == "s":
    s = open("scores.txt","r")

    file_content = s.read().splitlines()

    users_points = {i.split()[0]: int(i.split()[2]) for i in file_content}
    best_player = max(users_points.items(), key=operator.itemgetter(1))[0]
    print("LeaderBoard: ")
    print("\n")
    print('player with maximum points is {}, this player has {} points'.format(best_player, users_points[best_player]))
    best_players = sorted(users_points, key=users_points.get, reverse=True)
    for bp in best_players:
        print('{} has {} points'.format(bp, users_points[bp])) # This prints all players scores

if ens == "n":
    username=input("Please enter appropiate username: ")
    password1=input("Please enter password: ")
    password2=input("Please re-enter password: ")
    if password1 == password2: # checking if both passwords entered are the same
        print("your account has been successfully been made Thankyou")
        file = open("accountfile.txt","a")
        file.write("username: ")
        file.write(username)
        file.write(" ")
        file.write("password: ")
        file.write(password2)
        file.write("\n")
        file.close()
        print("Please enter 'n' if you are a new user and 'e' if you are a exsiting user")
        ens=input(" ")
    if password1 != password2: # if passwords entered are not the same will loop until they are correctly entered
        correctPassword=(password1)
        while True:
            password=input('Enter password again ')
            if password == correctPassword:
                print('Correct password has been entered')
                f = open ("accountfile.txt","a+")
                f.write("username: ")
                f.write(username)
                f.write(" ")
                f.write("password: ")
                f.write(correctPassword)
                f.write("\n")
                f.close()
                print("Please enter 'n' if you are a new user and 'e' if you are a exsiting user")
                en=input(" ")
            print('Incorrect password ')

if ens == "e":
    counter = 0
    check_failed = True
    while check_failed:
        print("Could player 1 enter their username and password")
        username1=input("Please enter your username ")
        password=input("Please enter your password ")
        with open("accountfile.txt","r") as username_finder:
            for line in username_finder:
                if ("username: " + username1 + " password: " + password) == line.strip():
                    print("you are logged in")
                    check_failed = False
                    counter = 0
                    check_failed = True
                    while check_failed:
                        print("Could player 2 enter their username and password")
                        username2=input("Please enter your username ")
                        password=input("Please enter your password ")
                        with open("accountfile.txt","r") as username_finder:
                            for line in username_finder:
                                if ("username: " + username2 + " password: " + password) == line.strip():
                                    print("you are logged in")
                                    check_failed = False
                                    time.sleep(1)
                                    print("Welcome to the dice game")
                                    time.sleep(1)
                                    while rounds < 5:
                                        total_score2 = total_score2 + playerTwoPoints
                                        total_score1 = total_score1 + playerOnePoints
                                        rounds = rounds + 1
                                        number = random.randint(1,6)
                                        number2 = random.randint(1,6)
                                        playerOnePoints = number + number2
                                        print("Round",rounds)
                                        print("-------------------------------------------")
                                        print("Player 1's turn    Type 'roll' to roll the dice")
                                        userOneInput = input(">>> ")
                                        if userOneInput == "roll":
                                            time.sleep(1)
                                            print("Player 1's first roll is", number)
                                        print("Player 1's second roll    Type 'roll' to roll the dice")
                                        userOneInput = input(">>> ")
                                        if userOneInput == "roll":
                                            time.sleep(1)
                                            print("player 1's second roll is", number2)
                                        if playerOnePoints <= 0:
                                                playerOnePoints = 0
                                        if playerOnePoints % 2 == 0:
                                            playerOnePoints = playerOnePoints + 10
                                            print("Player 1's total is even so + 10 points")
                                            print("-------------------------------------------")
                                            print("Player 1 has",playerOnePoints, "points")
                                        else:
                                            playerOnePoints = playerOnePoints - 5
                                            print("player 1's total is odd so -5 points")
                                            print("-------------------------------------------")
                                            print("Player 1 has",playerOnePoints, "points")
                                            if playerOnePoints <= 0:
                                                playerOnePoints = 0
                                        number = random.randint(1,6)
                                        number2 = random.randint(1,6)
                                        playerTwoPoints = number + number2
                                        print("-------------------------------------------")
                                        print("Player 2's turn    Type 'roll' to roll the dice")
                                        userTwoInput = input(">>> ")
                                        if userTwoInput == "roll":
                                            time.sleep(1)
                                            print("Player 2's first roll is", number)
                                        print("Player 2's second roll    Type 'roll' to roll the dice")
                                        userTwoInput = input(">>> ")
                                        if userTwoInput == "roll":
                                            time.sleep(1)
                                            print("player 2's second roll is", number2)
                                        if playerTwoPoints <= 0:
                                                playerTwoPoints = 0
                                        if playerTwoPoints % 2 == 0:
                                            playerTwoPoints = playerTwoPoints + 10
                                            print("Player 2's total is even so + 10 points")
                                            print("-------------------------------------------")
                                            print("Player 2 has",playerTwoPoints, "points")
                                        else:
                                            playerTwoPoints = playerTwoPoints - 5
                                            print("player 2's total is odd so -5 points")
                                            print("-------------------------------------------")
                                            print("Player 2 has",playerTwoPoints, "points")
                                            print("-------------------------------------------")

                                    print("Total score for player 1 is", total_score1)
                                    print("-------------------------------------------")
                                    print("Total score for player 2 is", total_score2)
                                    print("-------------------------------------------")

                                    if total_score1 > total_score2:
                                        print("Player 1 Wins!")
                                        file = open("scores.txt","a")
                                        file.write(username1)
                                        file.write(" has ")
                                        file.write(str(total_score1))
                                        file.write(" points")
                                        file.write("\n")
                                        file.close()
                                        sys.exit()
                                    if total_score2 > total_score1:
                                        print("Player 2 Wins!")
                                        file = open("scores.txt","a")
                                        file.write(username2)
                                        file.write(" has ")
                                        file.write(str(total_score2))
                                        file.write(" points")
                                        file.write("\n")
                                        file.close()
                                        sys.exit()
                                    if total_score1 == total_score2:
                                        print("Its a draw!")
                                        print("So both players will have to roll one more dice")
                                        time.sleep(2)
                                        print("-------------------------------------------")
                                        print("Player 1's turn    Type 'roll' to roll the dice")
                                        userOneInput = input(">>> ")
                                        if userOneInput == "roll":
                                            time.sleep(1)
                                            print("Player 1's first roll is", number)
                                        print("Player 1's second roll    Type 'roll' to roll the dice")
                                        userOneInput = input(">>> ")
                                        if userOneInput == "roll":
                                            time.sleep(1)
                                            print("player 1's second roll is", number2)
                                        if playerOnePoints % 2 == 0:
                                            playerOnePoints = playerOnePoints + 10
                                            print("Player 1's total is even so + 10 points")
                                            print("-------------------------------------------")
                                            print("Player 1 has",playerOnePoints, "points")
                                        else:
                                            playerOnePoints = playerOnePoints - 5
                                            print("player 1's total is odd so -5 points")
                                            print("-------------------------------------------")
                                            print("Player 1 has",playerOnePoints, "points")
                                        number = random.randint(1,6)
                                        number2 = random.randint(1,6)
                                        playerTwoPoints = number + number2
                                        print("-------------------------------------------")
                                        print("Player 2's turn    Type 'roll' to roll the dice")
                                        userTwoInput = input(">>> ")
                                        if userTwoInput == "roll":
                                            time.sleep(1)
                                            print("Player 2's first roll is", number)
                                        print("Player 2's second roll    Type 'roll' to roll the dice")
                                        userTwoInput = input(">>> ")
                                        if userTwoInput == "roll":
                                            time.sleep(1)
                                            print("player 2's second roll is", number2)
                                        if playerTwoPoints % 2 == 0:
                                            playerTwoPoints = playerTwoPoints + 10
                                            print("Player 2's total is even so + 10 points")
                                            print("-------------------------------------------")
                                            print("Player 2 has",playerTwoPoints, "points")
                                        else:
                                            playerTwoPoints = playerTwoPoints - 5
                                            print("player 2's total is odd so -5 points")
                                            print("-------------------------------------------")
                                            print("Player 2 has",playerTwoPoints, "points")
                                            print("-------------------------------------------")
                                        if total_score1 > total_score2:
                                            print("Player 1 Wins!")
                                            file = open("scores.txt","a")
                                            file.write(username1)
                                            file.write(" has ")
                                            file.write(str(total_score1))
                                            file.write(" points")
                                            file.write("\n")
                                            file.close()
                                        if total_score2 > total_score1:
                                            print("Player 2 Wins!")
                                            file = open("scores.txt","a")
                                            file.write(username2)
                                            file.write(" has ")
                                            file.write(str(total_score2))
                                            file.write(" points")
                                            file.write("\n")
                                            file.close()
                                            sys.exit()
                            else:
                                print("Sorry, this username or password does not exist please try again")
                                counter = counter + 1
                                if counter == 3:
                                    print("----------------------------------------------------")
                                    print("You have been locked out please restart to try again")
                                    sys.exit()

            else:
                print("Sorry, this username or password does not exist please try again")
                counter = counter + 1
                if counter == 3:
                    print("----------------------------------------------------")
                    print("You have been locked out please restart to try again")
                    sys.exit()
