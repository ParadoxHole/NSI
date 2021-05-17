def ex1():
    nom_prenom = input ("Entrez vos noms et prénoms séparés pas un espace : ")
    nom = nom_prenom.split(' ')[0]
    a = nom[0].upper()
    prenom = nom_prenom.split(' ')[1]
    b = prenom[0].upper()

    print(a,b)
    return 

def ex3():
    liste = [45,17,89,38,10,74]
    liste.sort()
    liste.append(12)
    for i in range (len(liste)//2):
        liste[i],liste[-i-1] = liste[-i-1],liste[i]
    print(liste)
    for i in range(len(liste)):
        if liste[i] == 10 :
            print(i)
            break

    print()
    liste.remove(38)
    print(liste[2:4])
    print(liste[:1])
    print(liste[2:])
    print(liste[-1])

    print(liste)
    return

def ex4_1(n):
    L=[]
    for i in range(n):
        L.append(1)
        L.append(i+1)
    return 

def ex4_2(n):
    L=[]
    for i in range(n):
        for j in range(i+1):
            L.append(j+1)
    return 

print(ex1())
print(ex3())
print(ex4_1(10))
print(ex4_2(10))