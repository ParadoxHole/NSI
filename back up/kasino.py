
import os
from random import randrange
from math import ceil

argent = 1000 
continuer_partie = True 

print("Vous vous installez à la table de roulette avec", argent, "$.")

while continuer_partie: 
    nombre_mise = -1
    while nombre_mise < 0 or nombre_mise > 49:
        nombre_mise = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 49) : ")
        try:
            nombre_mise = int(nombre_mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            nombre_mise = -1
            continue
        if nombre_mise < 0:
            print("Ce nombre est négatif")
        if nombre_mise > 49:
            print("Ce nombre est supérieur à 49")

    # on sélectionne la somme à miser sur le nombre
    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Tapez le montant de votre mise : ")
        # On convertit la mise
        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            mise = -1
            continue
        if mise <= 0:
            print("La mise saisie est négative ou nulle.")
        if mise > argent:
            print("Vous ne pouvez miser autant, vous n'avez que", argent, "$")

    # on fait tourner la roulette
    numero_gagnant = randrange(50)
    print("La roulette tourne... ... et s'arrête sur le numéro", numero_gagnant)

    # On établit la thune du joueur
    if numero_gagnant == nombre_mise:
        print("Félicitations ! Vous obtenez", mise * 3, "$ !")
        argent += mise * 3
    elif numero_gagnant % 2 == nombre_mise % 2: # ils sont de la même couleur
        mise = ceil(mise * 0.5)
        print("Vous avez misé sur la bonne couleur. Vous obtenez", mise, "$")
        argent += mise
    else:
        print("Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
        argent -= mise

    # On arrête la partie si le joueur est pauvre
    if argent <= 0:
        print("Vous êtes ruiné ! C'est la fin de la partie.")
        continuer_partie = False
    else:
        print("Vous avez à présent", argent, "$")
        quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")
        if quitter == "o" or quitter == "O" or quitter == "oui":
            print("Vous quittez le casino avec vos gains.")
            continuer_partie = False

# On met en pause le système (Windows)
os.system("pause")