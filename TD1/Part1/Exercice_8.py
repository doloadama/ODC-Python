#Importer le module math pour acceder à la racine carrée
from math import sqrt

#Afficher un message qui demande de saisir les points
Xa = input("Veuillez donner la coordonnée de A en abscisse: ")
Ya = input("Veuillez donner la coordonnée de A en ordonnée: ")
Xb = input("Veuillez donner la coordonnée de A en abscisse: ")
Yb = input("Veuillez donner la coordonnée de A en ordonnée: ")

#Calcul de la distance
distance = sqrt((Xb- Xa)^2 + (Yb - Ya)^2)

#Afficher la distance
print("la distance séparant les deux points est de: ", distance)
 