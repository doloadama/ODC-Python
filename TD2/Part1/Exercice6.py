#Demander à l'utilisateur de saisir des prix
prix = int(input("Veuillez sasisir un prix: "))
#initialisation des variables
somme = 0
while prix != 0:
    prix = int(input("Veuillez sasisir un prix: "))
    somme += prix
#Affichage de sa somme
print("la somme des prix des articles est de : ", somme)
