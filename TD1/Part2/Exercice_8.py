#Afficher un message pour receuillir l'année et le mois ainsi que le jour
while True:
    annee = input("Fournir une annee: ")
    if annee.isdigit() > 0:
        break
    else:
        print("Veuillez saisir une année correcte!")
annee = int(annee)

#Mois
while True:
    mois = input("Fournir un mois: ")
    if 1 <= mois.isdigit() <= 12:
        break
    else:
        print("Veuillez saisir un mois correcte!")
mois = int(mois)

#Jours
while True:
    jours = input("Fournir un jour: ")
    if 0 < jours.isdigit():
        break
    else:
        print("Veuillez saisir un jour correcte!")
jours = int(jours)


#Verifier si l'année est bisextile pour le mois de Fevrier
if annee % 4 == 0 or (annee % 400 == 0 and annee % 100 != 0):
    if mois == 2 and jours > 29:
        print("Le jour n'est pas valide")
    else:
        print("la date est valide")
else:
    if mois == 2 and jours > 28:
        print("le jour n'est pas valide")
    else:
        print("la date est valide")

#afficher les jours pour les mois de 31 jours
if mois in range(1, 7, 2) or mois in range(8 , 12, 2):
    if jours > 31:
        print("la date n'est pas valide")
    else:
        print("la date est valide")

#Afficher les jours pour les mois de 30 jours
if mois in range(2, 6, 2) or mois in range(9, 11, 2):
    if mois != 2 and jours > 30:
        print("la date n'est pas valide")
    else:
        print("la date est valide")
