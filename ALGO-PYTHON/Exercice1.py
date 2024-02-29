#Creation de listes contenant les mois en français et en anglais
mois_fr = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

mois_en = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#Afficher un message demandant de faire le choix
print("Voulez-vous afficher les mois en Français (F) ou en Anglais (A) ?")
choix = input("> ").upper()

mois = []
#Verifier le choix
if choix == "F":
  mois = mois_fr
elif choix == "A":
  mois = mois_en
else:
  mois = mois_fr

#Affichage du tableau
#Affichage de la première ligne
for i in range(0, 12, 3):
  print(f"{mois[i]:10}", end ="\t")
print()
k = 2

#Affichage de la deuxième ligne
for i in range(1, 12, 3):
  print(f"{mois[i]:10}", end ="\t")
print()
k = 2

#Affichage de la troisième ligne
for i in range(2, 12, 3):
  print(f"{mois[i]:10}", end ="\t")
print()
