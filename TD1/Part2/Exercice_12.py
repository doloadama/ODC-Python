#Afficher un message demandant à l'utilisateur de forunir les informations nécessaires
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

#Jours
while True:
   N = input("Fournir un jour: ")
   if 0 < N.isdigit():
       break
   else:
       print("Veuillez saisir un jour correcte!")
N = int(N)

# Liste des mois avec 31 jours
mois_31 = [1, 3, 5, 7, 8, 10, 12]

# Soustraire N jours à la date
jours -= N

# Vérifier si le jour est devenu négatif
while jours <= 0:
    mois -= 1
    if mois == 0:
        mois = 12
        annee -= 1
    if mois in mois_31:
        jours += 31
    elif mois == 2:
        if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
            jours += 29
        else:
            jours += 28
    else:
        jours += 30

# Afficher la date qu'il faisait il y a N jours
print("La date qu'il faisait il y a", N, "jours était :", jours, "/", mois, "/", annee)
