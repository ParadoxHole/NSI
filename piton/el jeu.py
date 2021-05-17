import random 
épée_actuelle = "rien"
alive = True
def c1():
    global épée_actuelle
    global alive
    nom = input("salutation jeune aventurier comment t'appelle tu ? > ")
    CueCOin = 100
    int(CueCOin)
    c1 = random.randint(0,100)
    if c1 > 0 and c1 < 20 :
        input ("je t'ai reconnue" + nom + " vas t'en je t'ai déjà dit de plus venir ici sale écuier")
        alive = False
    elif c1 >= 20 and c1 < 80 :
        input ("bienvenue dans la contrer du Cue "+ nom)
        input ("Tenez une épée de bois du cue")
        c1c4 = input ("VOULEZ VOUS EQUIPER L'ÉPÉE DE BOIS DU CUE ? > (répondez en minuscule)")
        if c1c4 == "oui":
            input ("VOUS AVEZ EQUIPÉ : ÉPÉE DE BOIS DU CUE")
            épée_actuelle = "épée_de_bois_du_cue"
            épée_actuelle = ""
        else :
            input ("VOUS N'AVEZ PAS EQUIPÉ : ÉPÉE DE BOIS DU CUE")
   
    else :
        c1c1 = input("hé wesh sa va fraire ienb ou ienb poto tu vien pour niké du dragon frère ? > ")
        if c1c1 == "oui":
            input("ben lets go reufré on y go")
            c2()
        else :
            c1c2 = input ("wesh t'es serieux frère j'ai plein d'épée légendaire regarde cel la seulement 10 diramme pas chère, pas chère t'es sur tu veux pas genre tiens un épée du cue, si tu veu dit oui > ")
            if c1c2 == "oui" :
                input ("VOUS GAGNER UNE ÉPÉE DU CUE, VOUS AVEZ DEPENSÉ 10 CUE-COINS")
                épée_actuelle = "épée_du_cue"
                CueCOin = CueCOin - 10
                input ("pa la peine de crié on avait compris ")
                input ("PARDON MAIS JE SUIS BLOQUÉ EN CAPS LOCK")
                c1c3 = input ("VOULEZ VOUS EQUIPER L'ÉPÉE DU CUE")
                if c1c3 == "oui":
                    input ("VOUS AVEZ EQUIPÉ : ÉPÉE DU CUE")
                    épée_actuelle = "épée_du_cue"
                else :
                    input ("VOUS N'AVEZ PAS EQUIPÉ : ÉPÉE DU CUE")
                c2()
            else :
                input ("éh ben ok nik")
                alive = False
def c2():
    if alive == True:
        c2 = input("UN SLIME APPARAIT ! QUE FAIRE ? : ATTAQUER(A) / FAIRE UN BISOUS(B) / EVITER(E)")
        if c2 == "A" and épée_actuelle == "épée_du_cue" :
            input ("VOUS ATTAQUER AVEC VOTRE ")
            input ("VOUS AVEZ TUER 'SLIME DÉGEULASSE' BIEN FAIT POUR LUI")
            input ("VOTRE " + épée_actuelle + "AS PRIS DES DEGATS ATTENTION")
            c3()
        elif c2 == "A" and épée_actuelle == "épée_de_bois_du_cue" :
            input ("VOUS ATTAQUER AVEC VOTRE épée_de_bois_du_cue, ELLE EST EN RÉALITÉ EN LATEX, VOUS NE FAITES AUCUN DEGATS ENCORE UNE SACRÉ FARCE DE GANDOULF LE VIEUX")
            input ("LE SLIM VOUS ATTAQUE ET VOUS FUYEZ COMME UN GOBLIN DU CUE")
            c3()
        elif c2 == "A" and épée_actuelle == "rien" :
            input ("MDR TA CRU QUOI QUE T'ALLER TUER UN SLIME AVEC TES MAINS")
            input ("VOUS ATTAQUER LE SLIME A MAN NUE")
            input ("EUH CA A MARCHER... BEN VOUS AVEZ GAGNER RIEN MDR")
            c3()
        elif c2 == "B" :
            input ("HEUUUUUUUUUUU SERIEUX ??? MAIS C'EST DEGEULASSE TU PEUX PAS FAIRE ÇA AAAAAAAAAAAAAH J'AI ENVIE DE VOMIR")
            input ("LE SLIME CE METS A ROUGIR (JE SUIS VRAIMENT OBLIGER DE DIRE ÇA C'EST PAS MOI QUI EST DÉCIDER)")
            input ("UNE ATTIRANCE SE RESSENT ENTRE VOUS DEUX (MAIS QUESQUE VOUS FAITE ENCORE LA JOUEUR PARTER C'EST HORRIBLE)")
            input ("VOUS VOUS DIRIGEZ VERS UNE ETBALE ET B**SER TOUTE LA NUIT (NON TOUT MES PAS ÇA TANT PIT JE VAIS DEVOIR OPTÉ POUR MA DENIÈRE SOLUTION -- DIVISION PAR ZERO --")
            input ("--")
            input ("--")
            input ("--")
            input ("--")
            input ("--")
            input ("HA vous avez eu un problème avec le jeu laisser moi finir")
            input ("vous forni*** avec le slime et avez beacoup de bébé slime/humain (ha ouais c'est dégeulasse)")
            input ("vous avez debloquer LA FIN MARRIAGE HEUREUX")
        else :
            input ("VOUS AVEZ EVITER LE SLIME, DIT DONC ÇA PRENDS DES RISQUES ICI HOULALA")
            input ("VOUS AVEZ DEBLOQUER LE SUCCÉS [SALE NUL]")
            c3()
def c3():
    global input
    print ("VOUS AVEZ PASSER LA FORET GRACE À UN PORTAIL MAGIC (TKT C MAGIK)")
    print ("FACE À VOUS 7 ENFANTS SE PRÉSENTENT (ON S'EN FOUT DES NOMS)")
    c3c1 = input ("LE PREMIER VOUS TENT UN BOBON VOUS ACCEPTEZ ? > ")
    if c3c1 == "oui":
        print ("VOUS ÊTES MORT")
        print ("EN MÊME TEMP FAUT ÊTRE CON POUR MANGER UN BONBON DONNER PAR UN ENFANT LOUCHE")
    else :
        input("OUI C'EST UNE BONNE IDÉE TRÈS BON CHOIX")  
          
    print = ("LE DEUXIÊME Vous parle pas lol")
   
    c3c3 = input = ("LE TROISIEME VOUS FRAPPE VOULEZ VOUS VOUS VENGER")
    if c3c3 == "oui" :
        print = ("VOUS FRAPPER L'ENFANT IL TOMBE AU SOL")                       
        print =("DES ELFES, DES ORCS, DES GOBLINS,TOUTES LES RACES DE LA CONTRER DU CUE ENFAITES SORTENT DE DERRIERES LES ARBRES ET VOUS APLAUDISSENT POUR VOTRE PROUÈSSE")
    elif c3c3 == "non" :
        print ("AH LA VICTIME IL SE FAIT FRAPPER PAR UN ENFANT")
        input ("VOUS AVEZ DEBLOQUER LE SUCCÉS [VICTIME]")
    else :
        print ("Wesh")
    print ("LE QUATRIEME MONTE À UN ARBRE ")
    print ("VOUS LE REGARDER LENTEMENT MONTER À LARBRE")
    print ("IL SAUTE DE L'ARBRE EN CRIANT :")
    print ("1")
    print ("2")
    print ("3")
    print ("alkaida")
    print ("VOUS L'ESQUIVER DE PEU ET IL PART EN CRIANT DES INVOCATIONS SATANIQUES")
    print ("LE CINQUIEME DAB")
    c3c4 = print ("LE FRAPPER ? > ")
    if c3c4 == "oui":
        print ("CHE")
    else :
        print ("HEU BEN OK DOMMAGE MOI JE L'AURAIS FRAPPER A VOTRE PLACE")
        print ("ENFIN JE DIT CA JE DIT RIEN")
    print  ("LE SIXEME")
    c3c5 = input ("PFF CEST LONG BON LES 2 DERNIERS VOUS INDIQUE LA DIRECTION VOUS LES SUIVEZ ? > ")
    if c3c5 == "oui" :
        print ("VOUS LES SUIVEZ ET IL VOUS INVITE À RENTRER CHEZ EUX")
        c3c6 = input ("VOULEZ VOUS RENTREZ ? >")
        if c3c6 == "oui" :
            print ("VOUS RENTRER DANS LA MAISON")
            print ("VOTRE TÊTE CE METS À TOURNER")
            c3c7 = input ("SE PLANTER LA JAMBE AVEC UN COUTEAU (A),FAIRE UN DAB(B)")
            if c3c7 == "A" :
                global épée_actuelle
                print ("TRES BONNE IDEE! LA DOULEUR VOUS REVEILLE ET VOUS VOUS TROUVEZ FACE AU 2 ENFANTS AVEC DES COUTEAU QUE FAIRE")
                c3c8 = input ("ATTAQUER (A), FUIR (B)")
                if c3c8 == "A" and épée_actuelle == "épée_du_cue" :
                    print ("VOUS ATTAQUER AVEC VOTRE épée_du_cue")
                    print ("VOUS AVEZ TUER LES ENFANTS DE SATAN, VOUS AVEZ LIBERE LE MONDE DES ENFANTS DE SATAN")
                 
                    print ("VOUS AVEZ DEBLOQUER LE SUCCES [HERO]")
                    print ("VOTRE " + épée_actuelle + "AS PRIS DES DEGATS ATTENTION")
                    c4()
                elif c3c8 == "A" and épée_actuelle == "épée_de_bois_du_cue" :
                    print ("VOUS ATTAQUER AVEC VOTRE épée_de_bois_du_cue, ELLE EST EN RÉALITÉ EN LATEX, VOUS EFRAYEZ LES ENFANTS AVEC LE LATEX CA LEUR RAPELLE DE MAUVAIS SOUVENIR. MERCI GANDOULF LE VIEUX")
                    print ("BRAVO VOUS AVEZ VAINCU TOUT LES ENFANTS DE SATAN, A OUI J'AI OUBLIAIS DE VOUS DIRE QUE C'ETAIT LES ENFANTS DE SATAN")
                    c4()
                elif c3c8 == "A" and épée_actuelle == "rien" :
                    print ("VOUS AGITER FRENETIQUEMENT LES BRAS DANS LES AIRS")
                    print ("LES ENFANTS PRENNENT PEUR ET VOUS DONNE :")
                    print ("epee_de_fukin_satan")
                    c3c9 = input ("VOULEZ VOUS EQUIPER epee_de_fukin_satan")
                    if c3c9 == "oui" :
                        épée_actuelle = "épée_de_fukin_satan"
                        c4()
                    else :
                        "L'ÉPÉE DE SATAN PREND LE CONTRÔLE DE VOTRE CORPS ET VOUS TUE"
            else :
                print ("SÉRIEUX UN DAB ???")
                print ("BEN TU SAIS QUOI TA GAGNER ALLER VAS DANS LE VILLAGE")
                c4() 
        else :
          print ("HOPE LA FUITE")
          c4()
     
    else :
        print ("bon choix")
        c4()
         
def c4() :
    input ("ui")            
         
c3()
#roi parceque tu vend épée de satan doit refuser toute tantation vous avez gagner en etant un roi heireux etbloin de toute tentation