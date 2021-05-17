from random import *
print ("c'est partie pour leuuuuu SHI... MU...FI")
score_ord = 0
score_player = 0

while score_player < 3 or score_ord < 3 :
    array = ["pierre","papier","ciseaux"]
    choix_ord = choice(array)
    choix_player = input("choisi un signe : pierre, papier; ciseaux > ")
    if choix_ord == choix_player :
        print ("égalité " + choix_player + " = " + choix_ord)
    elif choix_ord == "pierre" and choix_player == "ciseaux" :
        print ("CHE ta perdu, la pierre bats les ciseaux")
        score_ord += 1
    elif choix_ord == "ciseaux" and choix_player == "papier" :
        print ("CHE ta perdu, les ciceaux bats le papier")
        score_ord += 1
    elif choix_ord == "papier" and choix_player == "pierre" :
        print ("CHE ta perdu, la papier bats la pierre")
        score_ord += 1
    elif choix_player == "papier" and choix_ord == "pierre" :
        print ("bah c'est la chance du débutant qui débute, la papier bats la pierre")
        score_player += 1
    elif choix_player == "ciseaux" and choix_ord == "papier" :
        print ("bah c'est la chance du débutant qui débute, les ciceaux bats le papier")
        score_player += 1
    elif choix_player == "papier" and choix_ord == "pierre" :
        print ("bah c'est la chance du débutant qui débute, la papier bats la pierre")
        score_player += 1
    else :
        print ("heu je sais pas ce qui c'est passé")

if score_player = 3 :
    print("wesh ta triché")
else :
    print("CHEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")

