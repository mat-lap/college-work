import math

def resoudre(a, b, x):
    x = -b / a 
    print(round(x, 2))


a=0
b=0
x=0
choix='oui'
continuer=bool(choix=='oui')


while continuer is True :
    a = 0
    while a == 0 :
        a = int(input("Entrez a : "))
        if a == 0 :
            print("Erreur")
    b = int(input("Entrez b : "))
    resoudre(a, b, x)
    choix = input('Reprendre un autre calcul? (oui / non) : ')






