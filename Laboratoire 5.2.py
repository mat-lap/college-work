##Exercice 2 :
##Écrire un programme en Python, qui permet d’échanger le contenu de deux variables de type str

str1=''
str2=''
switchedstr=''

str1=input('entrez la Variable 1 : ')
str2=input('entrez la Variable 2 : ')
switchedstr=str1
str1=str2
str2=switchedstr
print('str1 : ', str1, 'str2 : ', str2)

