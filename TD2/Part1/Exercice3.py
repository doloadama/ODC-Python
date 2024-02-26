#Demander un nombre a
#Vérifier que ce nombre est positif
while True:
    a = input("Veuillez fournir un nombre entier: ")
    if a.isdigit() > 0:
        break
    else:
        print("Le nombre n'est pas valide!")
a = int(a)

#Demander un nombre b
#Vérifier que ce nombre est positif
while True:
    b = input("Veuillez fournir un nombre entier: ")
    if b.isdigit() > 0 :
        break
    elif a > b:
        break
    else:
        print("Le nombre n'est pas correct")
b = int(b)

#Initialisation des variables
moins = 0

#Calcul de la division
while a > 0:
    moins += 1
    a = a - b

#Affichage du résultat
print("La division de ", a, "par ", b" donne: ", moins)
