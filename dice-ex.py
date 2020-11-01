import random
import time
import sys


print("*****************Welcome To The DICE Game*******************")
abc=input("please type in 'n' if your are a new user type 'e' if you are a existing user: ")
while abc not in ('e','n'):
    abc=input("please type in 'n' if your are a new user type 'e' if you are a existing user: ")



if abc =="n":
    print("make an account")
    username=input("type in a username: ")
    password1=input("type in a pasword: ")
    password2=input("renter the password: ")
    if password1==password2:
        print("your password is",password1)
        f = open ("username + password.txt","a+")
        f.write(f"{username}:{password2}\n")
        f.close()
        abc=input("please type in 'n' if your are a new user type 'e' if you are a existing user: ")
    else:
        print("the password you entered is not matching restart the program to start again")
        sys.exit()

if abc == "e":
    check = True
    while check:
        print("player 1 enter your details")
        username1=input("Username = ")
        password=input("Password = ")
        with open("username + password.txt","r") as username_finder:
            for line in username_finder:
                if(username1 + ":" + password) == line.strip():
                    print("you are logged in")
                    print("player 2 enter your details")
                    while check:
                        print("incoreect password or username please try again")
                        username2=input("Username = ")
                        password=input("Password = ")
                        with open("username + password.txt","r") as username_finder:
                            for line in username_finder:
                                if(username2 + ":" + password) == line.strip():
                                    check = False

                                    print("you are logged on")

                                    #game
                                    player1=0
                                    player2=0
                                    print("*****************Welcome To The DICE Game*******************")


                                    print("PLAYER 1 READY")
                                    time.sleep(1)
                                    print("PLAYER 2 READY")

                                    totalscore1=0
                                    totalscore2=0



                                    #player 1

                                    dice1 = random.randint(1,6)
                                    dice2 = random.randint(1,6)
                                    roundno = 1
                                    while roundno < 5:
                                        totalscore1=totalscore1+player1
                                        totalscore2=totalscore2+player2
                                        player1=dice1+dice2
                                        roundno=roundno+1
                                        print("round",roundno)
                                        time.sleep(1)
                                        print("-----------------------------------------------------")
                                        asdf = input("player 1, press enter to roll")
                                        print("player 1 is rolling")
                                        print("player 1's first roll is",dice1)
                                        time.sleep(1)
                                        print("player 1's second roll is",dice2)
                                        time.sleep(1)
                                        print("-----------------------------------------------------")
                                        if player1 %2==0:
                                            print("This is an even number. so +10 points")
                                            time.sleep(1)
                                            player1=player1+10
                                            time.sleep(1)
                                            print("score is",player1)
                                            if player1<= 0:
                                                print("you have lost the game")
                                                sys.exit()
                                            print("-----------------------------------------------------")

                                        else:
                                            print("This is an odd number.")
                                            time.sleep(2)
                                            player1=player1-5
                                            print("score is",player1)
                                            time.sleep(3)
                                            print("player 1 score",player1)
                                            print("-----------------------------------------------------")



                                        time.sleep(1)
                                        #player 2
                                        dice1 = random.randint(1,6)
                                        dice2 = random.randint(1,6)
                                        totalscore1=totalscore1+player1
                                        totalscore2=totalscore2+player2
                                        player2=dice1+dice2
                                        print("-----------------------------------------------------")
                                        asdf = input("player 2 press enter to roll")

                                        print("player 2 is rolling")
                                        time.sleep(1)
                                        print("player 2's first roll is",dice1)
                                        time.sleep(1)
                                        asdf = input("player 2 press enter to roll again")
                                        time.sleep(1)
                                        print("player 2's second roll is",dice2)
                                        time.sleep(1)
                                        print("-----------------------------------------------------")

                                        if player2 %2==0:
                                            print("This is an even number. so +10 points")
                                            time.sleep(1)
                                            player2=player2+10
                                            print("score is",player2)
                                            time.sleep(1)
                                            if player2<= 0:
                                                print("you have lost the game")
                                                sys.exit()
                                            print("-----------------------------------------------------")

                                        else:
                                            print("This is an odd number.")
                                            time.sleep(1)
                                            player2=player2-5
                                            print("score is",player2)
                                            time.sleep(3)
                                            print("player 2 score",player2)
                                            print("-----------------------------------------------------")

                                    print("the total score for player 1 is ",totalscore1)
                                    print("the total score for player 2 is ",totalscore2)
                                    if totalscore1 > totalscore2:
                                        print("player 1 wins")
                                        file = open("scores.txt2","a+")
                                        file.write("player 1 ")
                                        file.write(username1)
                                        file.write(" has won overall with ")
                                        file.write(str(totalscore1))
                                        file.write(" points")
                                        file.write("\n")

                                    if totalscore2 > totalscore1:
                                        print("player 2 wins")
                                        file = open("scores.txt2","a+")
                                        file.write("player 2 ")
                                        file.write(username2)
                                        file.write(" has won overall with ")
                                        file.write(str(totalscore2))
                                        file.write(" points")
                                        file.write("\n")



                                else:
                                    print("incorrect username or password")

                else:
                    print("incorrect username or password")

