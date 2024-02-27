#Creation de listes contenant les mois en français et en anglais
mois_fr = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

mois_en = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#Afficher un message demandant de faire le choix
print("Voulez-vous afficher les mois en Français (F) ou en Anglais (A) ?")
choix = input("> ").upper()

#Verifier le choix
if choix == "F":
  mois = mois_fr
elif choix == "A":
  mois = mois_en
else:
  print("Choix invalide")
  exit()

#Affichage du tableau
for i in range(0, 11, 3):
  print(f"{mois[i]:10}", end ="\t")
print()

for i in range(1, 12, 3):
  print(f"{mois[i]:10}", end ="\t")
print()

for i in range(2, 12, 3):
  print(f"{mois[i]:10}", end ="\t")
print()
