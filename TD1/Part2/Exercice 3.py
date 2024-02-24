#Importer le module math pour utiliser la fonction racine carrée
from math import sqrt

#Afficher un demander A
A = int(input("Donner la valeur de A: "))
#Afficher un demander B
B = int(input("Donner la valeur de B: "))
#Afficher un demander C
C = int(input("Donner la valeur de C: "))

#Déclaration du discriminant et des solutions
delta = B^2 - 4*A*C
x1 = (-B + (sqrt(delta))) / (2*A)
x2 = (-B + (sqrt(delta))) / (2*A)
x0 = (-B/2*A)

#Vérification du résultat du discriminant et affichage des solutions
if delta < 0:
    print("Cette équation n'a pas de solution réelle")

if delta == 0:
    print("le discriminant = 0 donc cette équation admet une solution x0= ", x0)

else:
    print("L'équation admet deux solutions x1 = ", x1, "x2 = ", x2)
