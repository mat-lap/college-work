# liste vide

liste = [1]*10
print(liste)

#! pour manipuler les éléments d'une liste il faut utiliser les boucles 
#! toutes les listes commencent avec l'index 0
#! pour acceder aux éléments d'une liste, il faut d'abord mentionner son nom, suivi de l'index

#* taille

print(len(liste))
liste = [1, 2, 3, 4, 5, 6]

#* afficher ces éléments en utilisant la boucle while

i = 0
while (i < len(liste)):
    print(liste[i])
    i = i+1

#* affichage avec la boucle for

valeur = len(liste)

for valeur in liste:
    print(valeur)

#* trouver un élément dans la liste

liste = ['emp', 'Etudiant2', 'Etudiant3', 'Etudiant4']
if 'emp' in liste:
    print('existe')







