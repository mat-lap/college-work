##Exercice 1 :
##Écrire un programme en Python qui permet de trouver le plus grand nombre parmi 3 nombres entrés par l’utilisateur

n1=0
n2=0
n3=0
plusgrand=0


n1=int(input('Entrez le premier nombre : '))
n2=int(input('Entrez le deuxième nombre : '))
n3=int(input('Entrez le troisième nombre : '))
if n3>n1 and n3>n2:
    plusgrand=n3
elif n2>n1 and n2>n3:
    plusgrand=n2
else:
    plusgrand=n1
print(plusgrand)