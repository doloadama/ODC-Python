#Demander un nombre de départ
#Vérifier que ce nombre est positif
while True:
    nombre = input("Veuillez fournir un nombre entier: ")
    if nombre.isdigit() > 0:
        break
    else:
        print("Le nombre n'est pas valide!")
nombre = int(nombre)

#Initialisations des variables
somme = 0;

#Calcul de la somme
while nombre > 0:
    somme += nombre
    nombre -= 1

#Afficher la somme
print("la somme des précédents de ", nombre, "est de somme: ", somme)
