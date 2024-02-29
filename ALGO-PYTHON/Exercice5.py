import random
from colorama import init, Fore, Style
# Demander à l'utilisateur de saisir l'ordre de la matrice
while True:
    ordre = input("Entrez l'ordre de la matrice carrée : ")
    if ordre.isdigit() and int(ordre) > 0:
        break
    else:
        print("Veuillez saisir un nombre positif pour l'ordre de la matrice.")

# Convertir l'ordre en entier
ordre = int(ordre)

# Liste des couleurs et des positions
couleurs = ["bleu", "rouge"]
positions = ["HAUT", "BAS"]

# Demander à l'utilisateur de choisir la couleur
while True:
    couleur = input("Choisissez une couleur (bleu ou rouge) : ").lower()
    if couleur in couleurs:
        break
    else:
        print("Choix incorrect. Veuillez choisir une couleur parmi 'bleu' ou 'rouge'.")

# Demander à l'utilisateur de choisir la position
while True:
    position = input("Choisissez une position (HAUT ou BAS) : ").upper()
    if position in positions:
        break
    else:
        print("Choix incorrect. Veuillez choisir une position parmi 'HAUT' ou 'BAS'.")

# Créer une matrice carrée vide
matrice = []

# Remplir la matrice carrée avec des nombres aléatoires
for i in range(ordre):
    ligne = []
    for j in range(ordre):
        # Générer un nombre aléatoire entre 0 et 99 (vous pouvez ajuster selon vos besoins)
        nombre_aleatoire = random.randint(0, 9)
        ligne.append(nombre_aleatoire)
    matrice.append(ligne)

#Determination des diagonales
#Initialisations des variables représentants les diagonales
print (matrice)

principale = []
secondaire = []

for i in range(ordre):
    principale.append(matrice[i][i])  # Élément de la diagonale principale
    secondaire.append(matrice[i][ordre - 1 - i])  # Élément de la diagonale secondaire
