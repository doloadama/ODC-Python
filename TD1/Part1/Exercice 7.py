#Afficher un message demandant à l'utilisateur de donner les résistance
r1 = int(input("Veuillez saisir la première resistance: "))
r2 = int(input("Veuillez saisir la seconde resistance: "))
r3 = int(input("Veuillez saisir la troisième resistance: "))

#Calcul de la Resistance en Serie
serie = int(r1 + r2 + r3)

#calcul de la Resistance en parallèle
parallele = int((r1 * r2 * r3) / (r1*r2 + r2*r3 + r1*r3))

#Afficher les resultats
print("La résistance équivalente en série est de: ", serie)
print("La résistance équivalente en parallèle est de: ", parallele)
