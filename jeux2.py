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

    for i in range(tries):
        if i == 0:
            print("Programe Veuillez saisir un nombre")

        if nombrejoueur != secret:
            if random.choice([True, False]):
                print("Le programe reflechie...")
                time.sleep(random.randint(1,3))
                nombrejoueur = random.randint(minNUM, maxNUM)
                print("Le programme a pris", nombrejoueur)
            else:
                nombrejoueur = random.randint(minNUM, maxNUM)
                print("Le programme a choisie", nombrejoueur, "sans hesitation!")
                

        
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