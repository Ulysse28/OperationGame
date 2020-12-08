import random

#INTRODUCTION
print("Bonjour, tu vas t'entrainer aux mutiplications:")

#GENERER LES DEUX CHIFFRES AU HASARD ENTRE 1 ET 10



#ESSAI
score = 0

while score < 3:

    a = random.randint(1, 10)
    b = random.randint(1, 10)

    c = a * b
    print(a, "x", b, " = ?")
    rep = input()


    if int(rep) == c:
        print("OK")
        score = score + 1
    else:
        print("PAS OK")
        score = score + 1

    print("Bravo !!")

    score = 0

while score < 3:

    a = random.randint(1, 10)
    b = random.randint(1, 10)

    c = a * b
    print(a, "x", b, " = ?")
    rep = input()

    if int(rep) == c:
        print("OK")
        score = score + 1
    else:
        print("PAS OK")
        score = score + 1

    print("Bravo !!")