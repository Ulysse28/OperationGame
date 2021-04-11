"""
A little game to train yourself to mental calcul
Multiplications
Subtractions
Additions

By Ulysse Valdenaire
"""


import random

#Function MULTIPLICATIONS
def mul():
    print("You're going to train yourself to multiplication ! "
          " You have to reach a score of 10 to win ! ")
    score = 0
    while score < 10:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = a * b
        print(a, "x", b, " = ?")
        rep = input()
        if int(rep) == c:
            print("OK, that's right ! Keep going !")
            score = score + 1
            print(f"Your score is  {score}")
        else:
            print("NOT OK")
            score = score - 1
            print(f"Your score is {score}")

    print("Yeah ! You win !")


#Function ADDITIONS
def add():
    print("You're going to train yourself to additions ! You have to reach a score of 10 to win  !")
    score = 0
    while score < 10:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = a+b
        print(a, "+", b, " = ?")
        rep = input()

        if int(rep) == c:
            print("OK, that's right !")
            score = score + 1
            print(f"Your score is {score}")
        else:
            print("NOT OK !")
            score = score + 1
            print(f"Your score is {score}")

    print("Yeah ! You win !")



#Function SUBTRACTIONS
def sous():

    print("You're going to train yourself to subtraction ! "
          " You have to reach a score of ten to win the game !")

    score = 0
    while score < 10:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = a-b
        print(a, "-", b, " = ?")
        rep = input()

        if int(rep) == c:
            print("OK,You're right !")
            score = score + 1
            print(f"Your score is  {score}")
        else:
            print("NOT OK")
            score = score + 1
            print(f"Your score is {score}")

    print("Yeah ! You win !!")

#Main Menu

replay = ""

#Loop of the game
while replay != 'NO':

    level = input("In this game you can train yourself to multiplications,\n"
                    "additions and subtractions. You can begin by what you want:\n"
                  "Multiplications (M), Additions (A), Subtractions (S) : ")

#levels of the game
    if level == "M":
        mul()
        replay = input("Do you want to play again ? YES / NO ?")
    elif level == "A":
        add()
        replay = input("Do you want to play again ? YES / NO ?")
    elif level == "S":
        sous()
        replay = input("Do you want to play again ? YES / NO ?")
    else:
        print("ERROR")

#If the player quits the game
print("It was great playing with you ! See you around !")
    print("ERROR")
