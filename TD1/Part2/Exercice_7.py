#Afficher un message pour receuillir l'année et le mois
while True:
    annee = input("Fournir une annee: ")
    if annee.isdigit() > 0:
        break
    else:
        print("Veuillez saisir une année correcte!")

annee = int(annee)


#Initialisation du nombre de jours
jour = 0

while True:
    mois = input("Fournir un mois: ")
    if 1 <= mois.isdigit() <= 12:
        break
    else:
        print("Veuillez saisir un mois correcte!")

mois = int(mois)

#Verifier si l'année est bisextile pour le mois de Fevrier
if annee % 4 == 0 or (annee % 400 == 0 and annee % 100 != 0):
    if mois == 2:
        jour = 29
        print("le nombre de jour de ce mois est de ", jour, " jours")
else:
    if mois == 2:
        jour = 28
        print("le nombre de jour de ce mois est de ", jour, " jours")

#afficher les jours pour les mois de 31 jours
if mois in range(1, 7, 2) or mois in range(8 , 12, 2):
    jours = 31
    print("le nombre de jour de ce mois est de ", jour, " jours")

#Afficher les jours pour les mois de 30 jours
if mois in range(2, 6, 2) or mois in range(9, 11, 2):
    if mois != 2:
        jour = 30
        print("le nombre de jour de ce mois est de ", jour, " jours")
