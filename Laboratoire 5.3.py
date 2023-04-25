##Exercice 3 :
##Écrire un programme en Python pour demander à l’utilisateur d’entrer son nom et son prénom, 
##ensuite vérifier si c’est bien Desjardins Marcel, si oui on affiche un message de bienvenue, sinon afficher erreur.

nom=''
prenom=''
nomcorrect='Desjardins'
prenomcorrect='Marcel'
bonutilisateur=False
bienvenue='Bienvenue, {}, {}.'
erreur="Erreur! {}, {} n'est pas un utilisateur valide."

while bonutilisateur is False:
    nom=input('Entrez votre nom : ')
    prenom=input('Entrez votre prénom : ')
    if nom==nomcorrect and prenom==prenomcorrect:
        bonutilisateur=True
    else:
        print(erreur.format(nom, prenom))
print(bienvenue.format(nom, prenom))
