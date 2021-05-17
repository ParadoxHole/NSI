import random 
épée_actuelle = "rien"
alive = True
def c1():
    global épée_du_cue
    global alive
    nom = input("bonjour jeune aventurier comment t'appelle tu >")
    CueCOin = 100
    int(CueCOin)
    c1 = random.randint(0,100)
    if c1 > 0 and c1 < 20 :
        print ("je t'ai reconnue" + nom + " vas t'en je t'ai déjà dit de plus venir ici sale écuier")
        alive = False
    elif c1 >= 20 and c1 < 80 :
        print ("bienvenue dans la contrer du Cue "+ nom)
        print ("Tenez une épée de bois du cue")
        c1c4 = input ("VOULEZ VOUS EQUIPER L'ÉPÉE DE BOIS DU CUE")
        if c1c4 == "oui":
            print ("VOUS AVEZ EQUIPÉ : ÉPÉE DE BOIS DU CUE")
            épée_actuelle = "épée_de_bois_du_cue"
            str (épée_actuelle)
        else :
            print ("VOUS N'AVEZ PAS EQUIPÉ : ÉPÉE DE BOIS DU CUE")


        c2()
    else :
        c1c1 = input("hé wesh sa va fraire ienb ou ienb poto tu vien pour niké du dragon frère > ")
        if c1c1 == "oui":
            print("ben lets go reufré on y go")
            c2()
        else :
            c1c2 = input ("wesh t'es serieux frère j'ai plein d'épée légendaire regarde cel la seulement 10 diramme pas chère, pas chère t'es sur tu veux pas genre tiens un épée du cue, si tu veu dit oui > ")
            if c1c2 == "oui" :
                print ("VOUS GAGNER UNE ÉPÉE DU CUE, VOUS AVEZ DEPENSÉ 10 CUE-COINS")
                épée_du_cue = True
                CueCOin = CueCOin - 10
                print ("pa la peine de crié on avait compris ")
                print ("PARDON MAIS JE SUIS BLOQUÉ EN CAPS LOCK")
                c2()
                c1c3 = input ("VOULEZ VOUS EQUIPER L'ÉPÉE DU CUE")
                if c1c3 == "oui":
                    print ("VOUS AVEZ EQUIPÉ : ÉPÉE DU CUE")
                    épée_actuelle = "épée_du_cue"
                else :
                    print ("VOUS N'AVEZ PAS EQUIPÉ : ÉPÉE DU CUE")
            else :
                print ("éh ben ok nik")
                alive = False

def c2():
    if alive == True:
        c2 = input("UN SLIME APPARAIT ! QUE FAIRE ? : ATTAQUER(A) / FAIRE UN BISOUS(B) / EVITER(E)")
        if c2 == "A" and épée_du_cue == True :
            print ("VOUS ATTAQUER AVEC VOTRE ")
            print ("VOUS AVEZ TUER 'SLIME DÉGEULASSE' BIEN FAIT POUR LUI")
            print ("VOTRE " + épée_actuelle)
        

c1()