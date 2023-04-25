##Exercice 5 :
##Écrire un programme en Python, qui permet de réaliser une calculatrice élémentaire avec les quatre opérations +, -, *, / 

n1=0
n2=0
operation=''
resultat=0

n1=int(input('Entrez le premier nombre : '))
operation=input("Entrez l'opération à effectuer (+, -, *, /) : ")
n2=int(input('Entrez le deuxième nombre : '))

if operation=='+':
    resultat=n1+n2
elif operation=='-':
    resultat=n1-n2
elif operation=='*':
    resultat=n1*n2
elif operation=='/':
    resultat=n1/n2
print(resultat)