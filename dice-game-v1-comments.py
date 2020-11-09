# builtin fuction that need to be called
from random import randint
from time import sleep
from datetime import datetime
from csv import reader, DictWriter
from sys import exit
from os.path import isfile
from operator import itemgetter

# counter for the nume of rounds for each player
rounds = 0
# scores for players
score1 = 0
score2 = 0
#  scores for tie breaker
score1_tb = 0
score2_tb = 0
# dictionary to store users
users = {"raylin": "1234", "tommy": "1234", "luke": "1234"}

# set up the date for the game
# grad the date and time now
date = datetime.now()
# formats the date DD-MM-YYYY
game_date = (date.strftime("%d-%b-%Y"))

# ------------Welcome screen--------------------------------
# when the program first runs this check if the scores.csv exists if it exists it will print the menu
# because if you try to check the scores and this file is not there the program will crash
# CSV stands for comma seperated values
if isfile("scores.csv"):
    print("\n--------Welcome to Dice Game---------")
    print("1. Please enter 'n' to add new player")
    print("2. Please enter 'p' to play Dice Game")
    print("3. Please enter 's' to display top 5 players")
    print("4. Please enter 'q' to quit game")
else:
    # if scores.csv does not exist it creates the file and then prints menu
    # open file called scores.csv to append information to the file.
    with open("scores.csv", "a") as file:
        # set the headers for the csv file
        headers = ["Name", "Score", "Date"]
        # Writes the headers for the CSV file
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        # Writes the data for the CSV file
        csv_writer.writerow({
            "Name": "Raylin",
            "Score": "77",
            "Date": "06-Nov-2020"
        })
        print("\n--------Welcome to Dice Game---------")
        print("1. Please enter 'N' to add new player")
        print("2. Please enter 'P' to play Dice Game")
        print("3. Please enter 'S' to display top 5 players")
        print("4. Please enter 'Q' to quit game")

# if you thpe capital letter it will set to lower case3go
menu = input("\nPlease select option from menu: ").lower()
# checks that user has selected valid option from menu.
# while loop will run till valid option selected.
while menu not in ["n", "p", "s", "q"]:
    print(f"\n{menu}: is not a valid option ")
    menu = input("\nPlease select option from menu: ").lower()

if menu == "q":
    print("You have ended the game")
    exit()

if menu == "s":
    # opens the scores.csv file
    with open("scores.csv") as file:
        csv_reader = reader(file)
        # skips the frist row so headers are not printed on the scores
        next(csv_reader)
        # create the scores screen
        print("\n*****************TOP FIVE PLAYERS***************")
        print("*****Player****    ****Score****   \t****Date*****\n")
        # sorts the scores list in descending order
        # itemgetter used to pick point to sort om
        scores = sorted(csv_reader, reverse=True, key=itemgetter(1))
        print(scores)
        # slices scores list with onlu top five scores
        top = scores[0:5]
        # goes throught the list of scores and prints the top 5 players
        for t in top:
            print(f"{t[0]}\t\t\t{t[1]}\t\t{t[2]}")

        input("\nPress 'enter' to play Dice Game")

if menu == "n":
    username = input("Please enter username: ")
    pword1 = input("Please enter password: ")
    pword2 = input("Please re-enter password: ")
    # compares password1 to password2 to see if the match
    if pword1 == pword2:
        # if the match prints account created
        print("-------------------------------------------")
        print("User account successfully created")
        print("-------------------------------------------")
        # saves user to users dictionary
        users[username] = pword2
        input("\nPress 'enter' to play Dice Game")
    # if password1 and password2 dont match it take password one as
    # the correct password and asks for password2 again
    if pword1 != pword2:
        # takes password1 as correct password
        correct_pword = (pword1)
        print("Passwords did not match")
        pword2 = input("Enter password again: ")
        # compares password to the re entered password
        if pword2 == correct_pword:
            print("-------------------------------------------")
            print("User account successfully created")
            print("-------------------------------------------")
            # saves user to users dictionary
            users[username] = pword2
            input("\nPress 'enter' to play Dice Game")
        else:
            print("Incorrect password, please start again")
            exit()

# ------------------Player login-----------------------------

# check if user is logged in for while loop
check_failed = True
# While loop for user login
while check_failed:
    print("Player 1 enter their username and password")
    username1 = input("Please enter your username ")
    pword = input("Please enter your password ")
    # loop to get user key and password values fron the users dictionary
    for u, p in users.items():
        # compares the enterd username and password to the username and
        # password in users dictionary
        if u == username1 and p == pword:
            # sets username enterd to player1 whith capital first letter
            # if you enter a worng username or password it will keep asking
            # for one untill you enter a valid one
            player1 = username1.title()
            print("-------------------------------------------")
            print(f"Player #1 is {player1}")
            print("-------------------------------------------")
            # ends the while loop
            check_failed = False

            # # check if user is logged in for while loop
            check_failed = True
            while check_failed:
                print("Player 2 enter their username and password")
                username2 = input("Please enter your username ")
                pword = input("Please enter your password ")
                # loop to get user key and password values fron the
                # users dictionary
                for u, p in users.items():
                    # compares the enterd username and password to the username and
                    # password in users dictionary
                    if u == username2 and p == pword:
                        # sets username enterd to player1 whith capital first letter
                        # if you enter a worng username or password it will keep asking
                        # for one untill you enter a valid one
                        player2 = username2.title()
                        print("-------------------------------------------")
                        print(f"Player #2 is {player2}")
                        print("-------------------------------------------")
                        check_failed = False
                        sleep(2)
                        print("-------------------------------------------")
                        print("Dice Game Starting.......")
                        print("-------------------------------------------")
                        sleep(2)

# ------------Dice Game-------------------------------------

# While loop that will run for 5 rounds
while rounds < 5:
    # player one
    input(f"\n{player1} hit 'enter' roll dice")
    print("\nrolling......")
    print(f"\n--------{player1} Rolling Round #{rounds + 1}-----\n")
    # rolls dice1
    dice1 = randint(1, 6)
    # prints the total of dice one
    print(f"Dice #1 this round is: {dice1}")
    sleep(2)
    # rolls dice2
    dice2 = randint(1, 6)
    # prints the total of dice two
    print(f"Dice #2 this round is: {dice2}")
    sleep(2)
    # sums the total of dice1 and dice2
    total = dice1 + dice2
    #  compares the totals on each of the dice
    if dice1 == dice2:
        print("Adding 10 points for even total.")
        # the total is even 10 points is added to the score.
        total += 10
        print("Rolling dice again for double")
        # becauce the two dice are equal the player gets to
        # one extra die.
        dice3 = randint(1, 6)
        print(f"Extra roll total: {dice3}")
        # the total of the extra die is added
        total += dice3
        # check if the total is even using modulo
    elif total % 2 == 0:
        # if it is even 10 points are added
        total += 10
        print("Adding 10 points for even total.")
    else:
        # otherwise 5 points are subtracted
        total -= 5
        print("Subtracting 5 points for odd total.")
      #  prints the total for the round for player1
    print(f"Round total is: {total}")
    # add the total of this round for player1 to the score for player1
    score1 += total
    # score1 = 20
    print(f"Player score is: {score1}")
    print("-------------------------------------------")
    # checks if the player score is zero or less. if score is zero or less the
    # player automatically loses the game.
    if score1 <= 0:
        print("-------------------------------------------")
        print(f"{player1} your score is 0 or less")
        print(f"{player1} you have lost the game")
        print("-------------------------------------------")
        exit()

    # player 2
    input(f"\n{player2} hit 'enter' roll dice")
    print("\nrolling......")
    print(f"\n--------{player2} Rolling Round #{rounds + 1}-----\n")
    # rolls dice1
    dice1 = randint(1, 6)
     # prints the total of dice one
    print(f"Dice #1 this round is: {dice1}")
    sleep(2)
    # # rolls dice2
    dice2 = randint(1, 6)
     # prints the total of dice two
    print(f"Dice #2 this round is: {dice2}")
    sleep(2)
    # sums the total of dice1 and dice2
    total = dice1 + dice2
    #  compares the totals on each of the dice
    if dice1 == dice2:
        print("Adding 10 points for even total.")
        # the total is even 10 points is added to the score.
        total += 10
        print("Rolling dice again for double")
        # becauce the two dice are equal the player gets to
        # one extra die.
        dice3 = randint(1, 6)
        print(f"Extra roll total: {dice3}")
        # the total of the extra die is added
        total += dice3
    # check if the total is even using modulo
    elif total % 2 == 0:
        # if it is even 10 points are added
        total += 10
        print("Adding 10 points for even total.")
    else:
        # otherwise 5 points are subtracted
        total -= 5
        print("Subtracting 5 points for odd total.")
    #  prints the total for the round for player1
    print(f"Round total is: {total}")
    # add the total of this round for player2 to the score for player2
    score2 += total
    # score2 = 20
    print(f"Player score is: {score2}")
    print("-------------------------------------------")
    # checks if the player score is zero or less. if score is zero or less the
    # player automatically loses the game.
    if score2 <= 0:
        print("-------------------------------------------")
        print(f"{player2} your score is 0 or less")
        print(f"{player2} you have lost the game")
        print("-------------------------------------------")
        exit()
    rounds += 1


print("\n")
print("-------------------------------------------")
print(f"Total score for player 1 - {player1} is", score1)
print("-------------------------------------------")
print(f"Total score for player 2 - {player2} is", score2)
print("-------------------------------------------")

# ------------Tie break-------------------------------------

# compares player1 score to player2 score if the score is equal
if score1 == score2:
    print("Game Drawn")
    print("-------------------------------------------")
    print("\n************************TIE BREAK****************************")
    print("Each player rolls one die again to see who scores the highest")
    sleep(2)
    #  sets that there is no winner for the while loop
    no_win = True
    # while loop for tie break
    while no_win:
        input(f"\n{player1} hit 'enter' roll dice")
        print("\nrolling......")
        sleep(2)
        # rolls the tie break die for player1
        dice_tb1 = randint(1, 6)
        print(f"\n--------{player1} Tie Break--------\n")
        # sets the player1 score for the tie break to score to the total rolled
        score1_tb = dice_tb1
        print(f"{username1} rolled: {score1_tb}")
        # check if the total is even using modulo
        if score1_tb % 2 == 0:
            # if it is even 10 points are added
            score1_tb += 10
            print("Adding 10 points for even total.")
            print(f"{player1} score is: {score1_tb}")
        else:
            # otherwise 5 points are subtracted
            score1_tb -= 5
            print("Subtracting 5 points for odd total.")
            print(f"{player1} score is: {score1_tb}")
        # checks if the player score is zero or less. if score is zero or less the
        # player automatically loses the game.
        if score1_tb <= 0:
            print("-------------------------------------------")
            print(f"{player1} your score is 0 or less")
            print(f"{player1} you have lost the game")
            print("-------------------------------------------")
            # writes the player2 scores to scores.csv as they are the winner
            with open("scores.csv", "a") as file:
                headers = ["Name", "Score", "Date"]
                csv_writer = DictWriter(file, fieldnames=headers)
                csv_writer.writerow({
                    "Name": player2,
                    "Score": score2,
                    "Date": game_date
                })
                exit()

        input(f"\n{username2} hit 'enter' roll dice")
        print("\nrolling......")
        sleep(2)
        # rolls the tie break die for player2
        dice_tb2 = randint(1, 6)
        print(f"\n--------{player2} Tie Break--------\n")
         # sets the player1 score for the tie break to score to the total rolled
        score2_tb = dice_tb2
        print(f"{player2} rolled: {score2_tb}")
        # check if the total is even using modulo
        if score2_tb % 2 == 0:
            # if it is even 10 points are added
            score2_tb += 10
            print("Adding 10 points for even total.")
            print(f"{player2} score is: {score2_tb}")
        else:
            # otherwise 5 points are subtracted
            score2_tb -= 5
            print("Subtracting 5 points for odd total.")
            print(f"{player2} score is: {score2_tb}")
        # checks if the player score is zero or less. if score is zero or less the
        # player automatically loses the game.
        if score2_tb <= 0:
            print("-------------------------------------------")
            print(f"{player2} your score is 0 or less")
            print(f"{player2} you have lost the game")
            print("-------------------------------------------")
            # writes the player1 scores to scores.csv as they are the winner
            with open("scores.csv", "a") as file:
                headers = ["Name", "Score", "Date"]
                csv_writer = DictWriter(file, fieldnames=headers)
                csv_writer.writerow({
                    "Name": player1,
                    "Score": score1,
                    "Date": game_date
                })
                exit()
        # compares the player1 tie break score to the player2 tie break score
        if score1_tb == score2_tb:
            # if the scores are the same they will each have to roll again
            print("-------------------------------------------")
            print("Still no winner you will have to roll again")
            print("-------------------------------------------")
        # if player1 tie break score is greater than player2 tie brak score
        #  player1 wins
        elif score1_tb > score2_tb:
            # end while loop
            no_win = False
            print("-------------------------------------------")
            print(f"{player1} has won the Tie Break.")
            print("-------------------------------------------")
            # writes the player1 scores to scores.csv as they are the winner
            with open("scores.csv", "a") as file:
                headers = ["Name", "Score", "Date"]
                csv_writer = DictWriter(file, fieldnames=headers)
                csv_writer.writerow({
                    "Name": player1,
                    "Score": score1,
                    "Date": game_date
                })
                sys.exit()
        else:
            # otherwise player2 is the winner
            no_win = False
            print("-------------------------------------------")
            print(f"{player2} has won the Tie Break.")
            print("-------------------------------------------")
            # writes the player2 scores to scores.csv as they are the winner
            with open("scores.csv", "a") as file:
                headers = ["Name", "Score", "Date"]
                csv_writer = DictWriter(file, fieldnames=headers)
                csv_writer.writerow({
                    "Name": player2,
                    "Score": score2,
                    "Date": game_date
                })
                exit()
# if player1 score is greater than player2 score
#  player1 wins
elif score1 > score2:
    print(f"{player1} is the winner of this game.")
    print("-------------------------------------------")
    # writes the player1 scores to scores.csv as they are the winner
    with open("scores.csv", "a") as file:
        headers = ["Name", "Score", "Date"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writerow({
            "Name": player1,
            "Score": score1,
            "Date": game_date
        })
        exit()
# otherwise player2 is the winner
else:
    print(f"{player2} is the winner of this game.")
    print("-------------------------------------------")
    # writes the player2 scores to scores.csv as they are the winner
    with open("scores.csv", "a") as file:
        headers = ["Name", "Score", "Date"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writerow({
            "Name": player2,
            "Score": score2,
            "Date": game_date
        })
        exit()
