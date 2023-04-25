chaine=''
essais=3
nom=''
mdp=''
nomcorrect='mathis'
mdpcorrect='1234'
option=''
lettre=''

while nom != nomcorrect and mdp != mdpcorrect:
    for i in range(3):
        print("Il vous reste", essais, "essais.")
        nom = input("Entrez votre nom d'utilisateur : ")
        mdp = input("Entrez votre mot de passe : ")
        essais = essais - 1

option = input("Option A ou B? : ")
if option == 'A':
    chaine = input("Entrez une chaine de charactères : ")
    if chaine is type(str):
        lettre = input('Entrez une lettre : ')
        
        

