import random
import time

nombrejoueur=0

tries = 10
secret=0

maxNUM = 100
minNUM = 0

while True:
    print("Donnée un nombre que le program va devinée")
    secret = int(input())
    print("Combien d'essaie disponible (10 default)")
    tries = int(input())

    for i in range(tries):
        if i == 0:
            print("Programe Veuillez saisir un nombre")

        if nombrejoueur != secret:
            nombrejoueur = random.randint(minNUM, maxNUM)
            print("Le programme a choisie", nombrejoueur)
                

        
        if nombrejoueur == secret:
            print("Bravo Le programme a trouver en", i, "d'essaie!")
            break
        else:
            if nombrejoueur > secret:
                print("Le nombre secret est plus petit\n")
                maxNUM = nombrejoueur-1
            elif nombrejoueur < secret:
                print("Le nombre secret est plus grand\n")
                minNUM = nombrejoueur+1
    
    if nombrejoueur != secret:
        print("Vous êtes tombée a cour d'essait, le nombre était", secret)
    break