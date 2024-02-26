# Demande de la valeur de N
n = int(input("Entrez la valeur de N (entre 10 et 50): "))

# Vérification de la valeur de N
while n < 10 or n > 50:
  n = int(input("Valeur invalide. Entrez la valeur de N (entre 10 et 50): "))

# Saisie des nombres
nombres = []
for i in range(n):
  nombre = int(input(f"Entrez le nombre {i + 1}: "))

  # Vérification si le nombre est déjà saisi
  while nombre in nombres:
    nombre = int(input("Nombre déjà saisi. Entrez le nombre {i + 1}: "))

  # Ajout du nombre à la liste
  nombres.append(nombre)

# Initialisation de la longueur maximale de la séquence croissante
longueur_max = 1

# Initialisation de l'indice de début de la séquence maximale
indice_debut = 0

# Parcours de la liste
for i in range(1, n):

  # Comparaison de l'élément actuel avec l'élément précédent
  if nombres[i] > nombres[i - 1]:

    # Initialisation de la longueur de la séquence actuelle
    longueur_actuelle = 2

    # Parcours des éléments suivants
    for j in range(i + 1, n):

      # Comparaison des éléments suivants
      if nombres[j] > nombres[j - 1]:
        longueur_actuelle += 1
      else:
        # Fin de la séquence croissante
        break

    # Mise à jour de la longueur maximale et de l'indice de début si nécessaire
    if longueur_actuelle > longueur_max:
      longueur_max = longueur_actuelle
      indice_debut = i - 1

# Affichage du résultat
print(f"La longueur de la plus longue séquence croissante est de {longueur_max}")
print(f"La séquence est : ", end="")
for i in range(indice_debut, indice_debut + longueur_max):
  print(nombres[i], end=" ")
print()
