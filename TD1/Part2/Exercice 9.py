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

#Verifier si l'année est bisextile pour le mois de Fevrier
if annee % 4 == 0 or (annee % 400 == 0 and annee % 100 != 0):
   if mois == 2 and jours < 29:
       jour_suivant = jours + 1
   else:
       if mois == 2 and jours == 29:
           jour_suivant = 1
           mois = 3
else:
   if mois == 2 and jours < 28:
        jour_suivant = jours + 1

   else:
       if mois == 2 and jours == 28:
        jour_suivant = 1
        mois = 3

if mois == 12 and jours == 31:
    mois = 1
    annee += 1
    jour_suivant = 1

if mois in range(1, 7, 2) or mois in range(8, 12, 2):
    if mois != 12:
        if jours < 31:
            jour_suivant = jours + 1    
            mois += 1
        else:
            jour_suivant = 1    

if mois in range(4, 6, 2) or mois in range(9, 11, 2):
    if mois != 2:
        if jours < 30:
            jour_suivant = 1
            mois += 1
        else:
            jour_suivant = jours + 1

print("Le jour suivant est: ", jour_suivant, " / ", mois, " / ", annee)
