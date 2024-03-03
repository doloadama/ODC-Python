from Fonctions import*


# Initialisation de la liste d'étudiants
etudiants = []
# Menu principal
while True:
    print("\nMenu :")
    print("1. Saisir un nouvel étudiant")
    print("2. Afficher tous les étudiants")
    print("3. Trier et afficher par ordre décroissant de moyenne")
    print("4. Rechercher un étudiant (par téléphone, nom, prénom ou classe)")
    print("5. Modifier les notes d'un étudiant")
    print("6. Quitter")
    choix = input("Choisissez une option : ")

    if choix == "1":
        etudiants.append(saisie_etudiant())
    elif choix == "2":
        afficher_etudiants()
    elif choix == "3":
        trier_etudiants()
        afficher_etudiants()
    elif choix == "4":
        critere = input("Entrez le critère de recherche : ")
        etudiant = rechercher_etudiant(critere)
        if etudiant:
            print("Étudiant trouvé :")
            print(f"Nom : {etudiant['nom']}, Prénom : {etudiant['prenom']}, Classe : {etudiant['classe']}, Téléphone : {etudiant['tel']}")
        else:
            print("Aucun étudiant trouvé.")
    elif choix == "5":
        modifier_notes()
    elif choix == "6":
        print("Merci d'avoir utilisé notre application !")
        break
    else:
        print("Option invalide. Veuillez réessayer.")
