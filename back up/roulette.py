# -*- coding: utf-8 -*-

import random

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def isNumberValid(nbr, interval = False, firstNum = 0, SecondNum = 49):

    # si le nombre 2 est plus grand que le 1 on les échange
    if firstNum > SecondNum:
        temp = firstNum
        firstNum = SecondNum
        SecondNum = temp
        return False

    # On vérifie si le nombre est valide
    if RepresentsInt(nbr) == False:
        print(nbr+" n'est pas un nombre.")
        return False

    if (int(nbr) > firstNum or int(nbr) < SecondNum) and interval:
        print("Le nombre "+nbr+" n'est pas entre "+firstNum+" et "+SecondNum+".")
        return False

    return True

def roulette():
    nbr = ""   # definition de la variable du nombre choisi
    bille = "" # definition de la variable de la bille
    gain = 0   # definition du gain

    nbr = input("\nChoisis un numéro entre 0 et 49: ") # on fait choisir un nombre

    # on vérifie si il est valide (pas une string et entre 0 et 49)
    while isNumberValid(nbr, True) == False:
        nbr = input("\nChoisis un numéro entre 0 et 49: ")
    
    # on affiche le nombre choisi
    print("le nombre est "+nbr)

    # on fait choisir une mise
    mise = input("\nMaintenant mise une somme: ")

    # on vérifie si il est valide (pas une string)
    while isNumberValid(mise) == False:
        nbr = input("\nMaintenant mise une somme: ")

    # on affiche la mise choisie
    print("Ta mise est "+mise)

    # La bille est tirée au hasard
    bille = random.randint(0, 49)

    input("\nLa bille tirée est le numéro "+str(bille))

    # si la mise est bonne
    if (int(bille) == int(mise)):
        gain = 3 * int(mise)
        input("\nBravo vous avez parfaitement misé!\nVous remportez 3 fois votre mise\nc'est à dire "+str(gain))

    # si c'est la bonne couleur
    elif int(bille)%2 == int(nbr)%2:
        gain = 0.5 * int(mise)
        input("\nBravo vous avez misé sur la bonne couleur!\n\n> Vous remportez 0.5 fois votre mise,\nc'est à dire "+str(gain))
    
    else:
        gain = -int(mise)
        input("Dommage vous avez perdu!\nVous perdez votre mise\nc'est à dire "+str(mise))


roulette()