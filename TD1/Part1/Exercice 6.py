#Afficher un message demandant à l'utilisateur de saisir la longueur
longueur = input("Veuillez donner la longueur: ")
#Afficher un message demandant à l'utilisateur de saisir la largeur
largeur = input("Veuillez donner la largeur ")

"""#Vérication de la longueur
while not longueur.isdigit():
  print("Erreur : vous devez entrer un nombre entier.")
  longueur = input("Veuillez réessayer : ")

longueur= int(longueur)

while not longueur.isdigit():
  print("Erreur : vous devez entrer un nombre entier.")
  largeur= input("Veuillez réessayer : ")

largeur= int(largeur) 
"""

#Calcul du Périmètre
perimetre = (longueur + largeur) * 2

#Calcul de la surface
surface = (longueur * largeur)

#Afficher le périmètre et la surface
print("Le périmètre est de: ", perimetre)
print('La surface est de: ', surface)
