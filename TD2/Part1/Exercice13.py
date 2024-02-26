#Demander à l'utilisateur de saisir des prix
nombre = int(input("Veuillez sasisir un nombre: "))
#initialisation des variables
premier = 0; entiers = 0 ; i =0
liste_premiers = []
while nombre != 0:
    nombre = int(input("Veuillez sasisir un nombre: "))
    entiers =+ 1
    for i in range(2, nombre-1):
        if nombre % i == 0:
            break
        else:
            premier += 1
            liste_premiers.append(nombre)

print(f"la liste des nombres premiers saisis :{liste_premiers}\n"
      f"le nombre de nombre premiers saisis: {premier}"
      f"\nLe nombre d'entiers saisis {entiers}")
