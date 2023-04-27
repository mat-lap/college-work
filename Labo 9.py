# labo 9

#* Écrire un programme en python qui permet à l’utilisateur d’entrer la taille du tableau contenant des notes des étudiants,
#* et qui ensuite appelle une fonction qui calcule et retourne la moyenne de ces étudiants.
#* Validez les données 

# -------------------------------------------------------------------------------------------------------------------------
import math




def moyenne(len, somme):
    moyenne = somme / len
    return moyenne



notes = []
note = 0
nbnotes = 0
somme = 0
i = 0

nbnotes = int(input("Entrez le nombre de notes : "))

while i < nbnotes:
    notes.append(int(input("Entrez une note : "))) 
    if notes [i] < 0:
        print('Erreur, veuillez réessayer')
    else:
        somme = somme + notes [i]
        i = i + 1

print("La moyenne du groupe est de : ", moyenne(len(notes), somme))
