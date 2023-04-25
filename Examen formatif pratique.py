n1=0
n2=0
operation=''
resultat=0
stop=False
choix=''

while stop is False:
    n1=int(input('Entrez le premier nombre : '))
    operation=input("Entrez l'opération à effectuer (+, -, *, /) : ")
    n2=int(input('Entrez le deuxième nombre : '))
    if operation=='+':
        resultat=n1+n2
    elif operation=='-':
        if (n1-n2)<0:
            print("Erreur! Resultat négatif.")
        else:
            resultat=n1-n2
    elif operation=='*':
        resultat=n1*n2
    elif operation=='/':
        if n2==0:
            print("Erreur! Division par zéro.")
        else:
            resultat=n1/n2
    else:
        print('Erreur! Opération invalide.')
    print('Le résultat est : ', resultat)
    choix=input('Continuer? (O/N) : ')
    if choix=='N':
        stop=True
    elif choix=='O':
        stop=False
    else:
        stop=False
