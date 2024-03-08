import random #Gère la génération d'éléments de la matrice
from colorama import init, Fore, Style #Bibliothèque de gestion des couleurs
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

#Affichage de la matrice
def afficher_matrice(matrice):
    for ligne in matrice:
        for element in ligne:
            print(element, end=' ')
        print() 

#Determination des diagonales
#Initialisations des variables représentants les diagonales
print(f" ---------------------------------------------Voici la matrice-------------------------------------------\n {afficher_matrice(matrice)}")

principale = []
secondaire = []

#Recherche des éléments de la diagonale principale et secondaire 
for i in range(ordre):
    principale.append(matrice[i][i])  # Élément de la diagonale principale
    secondaire.append(matrice[i][ordre - 1 - i])  # Élément de la diagonale secondaire


"""Récupération des éléments suivants le premier élement sur
 la même ligne de la diagonale principale"""
suivants = []
for i in range(0, ordre):
    for j in range(i+1, ordre):
        suivants.append(matrice[i][j])

"""Récupération des éléments précedants dernier élement sur
 la même ligne de la diagonale principale"""
precedants = []
for i in range(0, ordre):
    for i in range(ordre - 2, -1, -1):
        precedants.append(matrice[ordre-1][i])


#Gestion de la coloration
# Initialiser colorama pour prendre en charge l'affichage des couleurs dans la console
init()

def afficher_liste_bleue(liste):
    for element in liste:
        # Imprimer l'élément en bleu
        print(Fore.BLUE + str(element), end=' ')
    # Réinitialiser les paramètres de couleur à la fin de l'impression de la liste
    return(Style.RESET_ALL)

def afficher_liste_rouge(liste):
    for element in liste:
        # Imprimer l'élément en bleu
        print(Fore.RED + str(element), end=' ')
    # Réinitialiser les paramètres de couleur à la fin de l'impression de la liste
    return (Style.RESET_ALL)

if couleur == "bleu":
    if position == "HAUT":
        print("Les éléments choisis sont là et hop: \n")
        print(afficher_liste_bleue(suivants))
    else:
        print("Les éléments choisis sont là et hop: \n")
        print(afficher_liste_bleue(precedants))
else:
    if position == "HAUT":
        print("Les éléments choisis sont là et hop: \n")
        print(afficher_liste_rouge(suivants))
    else:
        print("Les éléments choisis sont là et hop: \n")
        print(afficher_liste_rouge(precedants))
