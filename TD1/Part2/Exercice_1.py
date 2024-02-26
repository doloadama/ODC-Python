#Afficher un message demandant à l'utilisateur de faire un choix
# Demander la saisie de a
#Verifier si le choix est 1 ou 2
choix = input("choisissez entre l'option 1 ou 2: ")

"""
while True: # Tant que la condition dans la boucle est vraie
    choix = input("choisissez entre l'option 1 ou 2: ")
    if choix == 1 or choix == 2:
        break #sortir de la boucle
    else:
        print("Votre choix n'est pas correct")
"""

#Afficher un message demandant à l'utilisateur de donner les résistance
r1 = int(input("Veuillez saisir la première resistance: "))
r2 = int(input("Veuillez saisir la seconde resistance: "))
r3 = int(input("Veuillez saisir la troisième resistance: "))

if choix == 1:
    #Calcul de la Resistance en Serie
    serie = int(r1 + r2 + r3)
    #Afficher les resultats
    print("La résistance équivalente en série est de: ", serie)
else:
    #calcul de la Resistance en parallèle
    parallele = int((r1 * r2 * r3) / ((r1*r2) + (r2*r3) + (r1*r3)))
    print("La résistance équivalente en parallèle est de: ", parallele)


