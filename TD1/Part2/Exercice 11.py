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

#Initialisation
jour_suivant = 0


# Ajouter 5 jours à la date
jours += 5

# Liste des mois avec 31 jours
mois_31 = [1, 3, 5, 7, 8, 10, 12]

# Vérifier si le mois a dépassé sa longueur
if (mois in mois_31 and jours > 31) or (mois == 2 and jours > 29) or (mois not in mois_31 and jours > 30):
    jours -= 30
    mois += 1
    # Vérifier si l'année a dépassé 12 mois
    if mois > 12:
        mois -= 12
        annee += 1

# Afficher la date dans 5 jours
print("La date dans 5 jours sera :", jours, "/", mois, "/", annee)
