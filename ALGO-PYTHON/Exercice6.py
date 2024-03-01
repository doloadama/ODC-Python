from colorama import init, Fore

# Initialiser colorama pour prendre en charge l'affichage des couleurs dans la console
init()

# Tableaux de couleurs et de positions
couleurs = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
positions = ['ADDP', 'EDDP', 'SDP', 'ADDS', 'EDDS', 'SDS']

# Saisie de l'ordre de la matrice carrée
while True:
    ordre = input("Entrez l'ordre de la matrice carrée (supérieur à 4) : ")
    if ordre.isdigit() and int(ordre) > 4:
        ordre = int(ordre)
        break
    else:
        print("Veuillez saisir un nombre supérieur à 4 pour l'ordre de la matrice.")

# Affichage du menu de choix des positions
print("Menu de choix des positions :")
for i in range(len(positions)):
    print(f"{i+1}. {positions[i]}")

# Affichage du menu de choix des couleurs
print("\nMenu de choix des couleurs :")
for i in range(len(couleurs)):
    print(f"{i+1}. {couleurs[i]}{couleurs[i].__class__.__name__}{Fore.RESET}")

# Saisie de la position et de la couleur
while True:
    choix_position = input("Choisissez une position (1-6) : ")
    if choix_position.isdigit() and 1 <= int(choix_position) <= 6:
        position = positions[int(choix_position) - 1]
        break
    else:
        print("Veuillez saisir un nombre entre 1 et 6 pour choisir une position.")

while True:
    choix_couleur = input("Choisissez une couleur (1-6) : ")
    if choix_couleur.isdigit() and 1 <= int(choix_couleur) <= 6:
        couleur = couleurs[int(choix_couleur) - 1]
        break
    else:
        print("Veuillez saisir un nombre entre 1 et 6 pour choisir une couleur.")

# Création de la matrice avec des nombres de 1 à ordre*ordre
matrice = [[(i * ordre) + j + 1 for j in range(ordre)] for i in range(ordre)]

# Affichage de la matrice colorée
print("\nMatrice colorée :")
for ligne in matrice:
    for element in ligne:
        print(couleur + str(element), end=' ')
    print()  # Aller à la ligne après chaque ligne de la matrice
