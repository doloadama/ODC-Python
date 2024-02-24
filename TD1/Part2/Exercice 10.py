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


# Déterminer la date précédente
if jours > 1:
    jours -= 1
else:
    if mois > 1:
        mois -= 1
        # Liste des mois avec 31 jours
        if mois in [1, 3, 5, 7, 8, 10, 12]:
            jours = 31
        elif mois == 2:
            # Vérifier si l'année est bissextile
            if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
                jours = 29
            else:
                jours = 28
        else:
            jours = 30
    else:
        annee -= 1
        mois = 12
        jours = 31

# Afficher la date précédente
print("La date précédente est :", jours, "/", mois, "/", annee)
