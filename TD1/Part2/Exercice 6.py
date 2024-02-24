#Afficher un message damandant de saisir une année
#Verifier qu'il s'agit d'un nombre
while True:
    annee = input("Veuillez choisir une année: ")
    if annee.isdigit() > 0:
        break
    else:
        print("Choisir une année correcte!")

annee = int(annee)

#Verifier si l'année est bisextile ou pas et l'afficher
if annee % 4 == 0: 
    if(annee % 400 == 0 and annee % 100 != 0):
        print("L'année ", annee, " est bisextile")
else:
    print("L'année ", annee, " n'est pas bisextile")
