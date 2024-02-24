#Afficher un message demandant à l'utilisateur de saisir des secondes
#Contrôle de la valeur de saisie
while True:
    secondes = input("Veuillez saisir les secondes à convertir: ")
    if secondes.isdigit():
        break
    else:
        print("Valeur invalide. veuillez saisir un entier positif")

secondes = int(secondes)

#Conversion en heures
heures = int(secondes / (3600))
#Conversion en minutes
minutes = int((secondes % (3600)) / 60)
#Secondes restantes
secondes_bis = int((secondes % (3600)) % 60)

#Afficher le resultat
print("La conversion de ", secondes," secondes", "donne "
      , heures, " heures: ", minutes, " minutes: "
      , secondes_bis, " secondes")
