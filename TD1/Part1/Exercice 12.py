from datetime import datetime

# Afficher messsage de saisie des données de l'étudiant
nom = str(input("Nom: "))
prenom = str(input("Prénom: "))
jour_naissance = int(input("Jour de naissance: "))
mois_naissance = int(input("mois de naissance: "))
annee_naissance = int(input("année de naissance: "))

# Année en cours
annee_courante = 2024

# Calculer l'âge
age = annee_courante - annee_naissance
if (datetime.now().month, datetime.now().day) < (mois_naissance, jour_naissance):
    age -= 1

# Afficher les informations de l'étudiant
print("Nom de l'étudiant :", nom)
print("Prénom de l'étudiant :", prenom)
print("Date de naissance :", jour_naissance, "/", mois_naissance, "/", annee_naissance)
print("Âge :", age)
