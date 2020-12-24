import random

#MULTIPLICATIONS
def mul():
    print("Tu vas t'entraîner aux multiplications ! Ton but est d'atteindre le score de 10 !")
    score = 0
    while score < 10:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = a * b
        print(a, "x", b, " = ?")
        rep = input()
        if int(rep) == c:
            print("OK, tu as juste.")
            score = score + 1
            print(f"Ton score est de {score}")
        else:
            print("PAS OK")
            score = score - 1
            print(f"Ton score est de {score}")

    print("Bravo, tu as atteint 10 points !")

#ADDITIONS
def add():
    print("Tu vas t'entraîner aux additions ! Ton but est d'atteindre le score de 10 !")
    score = 0
    while score < 10:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = a+b
        print(a, "+", b, " = ?")
        rep = input()

        if int(rep) == c:
            print("OK? Tu as juste !")
            score = score + 1
            print(f"ton score est de {score}")
        else:
            print("PAS OK, c'est faux")
            score = score + 1
            print(f"ton score est de {score}")

    print("Bravo !! Tu as atteint 10 points !")

#SOUSTRACTIONS
def sous():
    score = 0
    print("Tu vas t'entraîner aux soustractions ! Ton but est d'atteindre le score de 10 !")

    while score < 10:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = a-b
        print(a, "-", b, " = ?")
        rep = input()

        if int(rep) == c:
            print("OK, tu as juste !")
            score = score + 1
            print(f"ton score est de {score}")
        else:
            print("PAS OK")
            score = score + 1
            print(f"ton score est de {score}")

    print("Bravo !! Tu as atteint 10 points")



#MENU PRINCIPAL
level = input("Dans ce jeu, tu peux t'entrainer aux multiplications,\n"
                "aux additions ou aux soustractions. Choisis en entrant une des trois lettre:\n"
              "Multiplivations (M), additions (A), soustractions (S) : ")

if level == "M":
    mul()
elif level == "A":
    add()
elif level == "S":
    sous()
else:
    print("ERROR")