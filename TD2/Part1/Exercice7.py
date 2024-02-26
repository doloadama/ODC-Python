# Initialisation
plus_grand = None
rang_plus_grand = None

# Demande des nombres à l'utilisateur
for i in range(10):
  nombre = int(input(f"Entrez le nombre {i + 1}: "))

  # Mise à jour du plus grand nombre et de son rang
  if plus_grand is None or nombre > plus_grand:
    plus_grand = nombre
    rang_plus_grand = i + 1

# Affichage du résultat
print(f"Le plus grand nombre est {plus_grand}")
print(f"Son rang dans la liste est {rang_plus_grand}")
