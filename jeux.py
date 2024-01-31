import random

nombrejoueur:int=0

tries = 10
secret= random.randint(1, 100)

while True:
    print("Deviner le nombre qui est entre 1 et 100... Vous avez 10 chance.")
    for i in range(tries):
        if i == 0:
            print("Veuillez saisir un nombre")

        if nombrejoueur != secret:
            nombrejoueur = int(input())

        if nombrejoueur == secret:
            print("Bravo")
            break
        else:
            if nombrejoueur > secret:
                print("Le nombre est plus petit")
            elif nombrejoueur < secret:
                print("Le nombre est plus grand")

    if nombrejoueur != secret:
        print("Vous êtes tombée a cour d'essait, le nombre était", secret)
    break