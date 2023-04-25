##Exercice 4 :
##Écrire un programme en Python, qui permet de classer 3 nombres dans l’ordre croissant

n1=0
n2=0
n3=0
petit=0
moyen=0
grand=0


n1=int(input('Entrez le premier nombre : '))
n2=int(input('Entrez le deuxième nombre : '))
n3=int(input('Entrez le troisième nombre : '))
if n1>n2 and n1>n3:
    grand=n1
if n1>n2 and n1<n3:
    moyen=n1
if n1<n2 and n1<n3:
    petit=n1
if n2>n1 and n2>n3:
    grand=n2
if n2>n1 and n2<n3:
    moyen=n2
if n2<n1 and n2<n3:
    petit=n2
if n3>n2 and n3>n1:
    grand=n3
if n3>n2 and n3<n1:
    moyen=n3
if n3<n2 and n3<n1:
    petit=n3
print(petit, moyen, grand)