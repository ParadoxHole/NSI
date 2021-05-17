# -*- coding: utf-8 -*-

def loubinaire(chiffre):
    binair=""
    while chiffre>0:
        binair = str(chiffre%2) + binair
        chiffre = chiffre//2
    return "le ciffre :" + binair

if __name__ == "__main__":
    print(loubinaire(int(input("chiffre :"))))