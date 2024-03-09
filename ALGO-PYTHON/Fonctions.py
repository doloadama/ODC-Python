#Gestion du numéro de téléphone
def number(num):
    """
    Fonction qui valide si le numéro de téléphone est correct.
    """
    commence = ["77", "78", "76", "70", "75"]  # Dépendances de début de numéro
    debutNumero = num[:2]
    return debutNumero in commence and len(num.replace(" ", "")) == 9

#Gestion de la validation de notes
def valider_note(note):
    """
    Fonction qui valide si la note est correcte.
    """
    return note.isdigit() and 0 <= float(note) <= 20

def gestion_string(mot):
    """Fonction qui gère la saisie du nom, prénom et la classe"""
    return mot != "" and mot !=" " and mot[0].isupper()
    
#Gestion de la saisie des informations des étudiants
def saisie_etudiant():
    """
    Fonction pour saisir les informations d'un étudiant.
    """
    while True:
        nom = input("Nom de l'étudiant : ")
        while not gestion_string(nom):
            print("Le nom doit commencer par une majuscule et ne comporte pas d'éspaces au début")
            nom = input("Nom de l'étudiant : ")
  
        prenom = input("Prénom de l'étudiant : ")
        while not gestion_string(prenom):
            print("Le prénom doit commencer par une majuscule et ne comporte pas d'éspaces au début")
            prenom = input("Prénom de l'étudiant : ")

        classe = input("Classe de l'étudiant : ")
        while not gestion_string(classe):
            print("Le nom de la classe doit commencer par une majuscule et ne comporte pas d'éspaces au début")
            classe = input("Classe de l'étudiant : ")

        # Validation du numéro de téléphone
        telephone = input("Téléphone de l'étudiant : ")
        while not number(telephone) or not telephone.isdigit():
            print("Format de numéro incorrect. Veuillez réessayer.")
            telephone = input("Téléphone de l'étudiant : ")

        # Validation des notes
        devoir = input("Note de devoir : ")
        while not valider_note(devoir):
            print("La note de devoir est incorrecte. Veuillez réessayer.")
            devoir = input("Note de devoir : ")

        projet = input("Note de projet : ")
        while not valider_note(projet):
            print("La note de projet est incorrecte. Veuillez réessayer.")
            projet = input("Note de projet : ")

        examen = input("Note d'examen : ")
        while not valider_note(examen):
            print("La note d'examen est incorrecte. Veuillez réessayer.")
            examen = input("Note d'examen : ")

        moyenne = round((float(devoir) + float(projet) + float(examen)) / 3)

        # Écrire les données de l'étudiant dans le fichier
        with open("donnees_etudiants.txt", "a") as fichier:
            fichier.write(f"{prenom}|{nom}|{classe}|{telephone}|{devoir}|{projet}|{examen}|{moyenne}\n")

        continuer = input("Voulez-vous ajouter un autre étudiant ? (O/N) : ")
        if continuer.upper() != "O":
            break

def afficher_etudiants():
    """
    Fonction pour afficher les informations de tous les étudiants.
    """
    print("\nListe des étudiants :\n")
    print()
    print("-" * 109)
    print("| {:<15} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10}|".format("Prénom", "Nom", "Classe", "Téléphone", "Devoir", "Projet", "Examen", "Moyenne"))
    print("-" * 109)

    with open("donnees_etudiants.txt", "r") as fichier:
        for ligne in fichier:
            prenom, nom, classe, telephone, devoir, projet, examen, moyenne = ligne.strip().split("|")
            print("| {:<15} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10.2}|".format(prenom, nom, classe, telephone, devoir, projet, examen, moyenne))
            print("-" * 109)

# Menu principal
def menu():
    """
    Fonction pour afficher le menu principal.
    """
    while True:
        print("\nMenu :")
        print("1. Saisir les informations d'un étudiant")
        print("2. Afficher tous les étudiants")
        print("3. Rechercher un étudiant (par téléphone, nom, prénom ou classe)")
        print("4. Trier par la moyenne")
        print("5. Modifier les notes d'un étudiant")
        print("6. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            saisie_etudiant()
        elif choix == "2":
            afficher_etudiants()
        elif choix == "3":
            critere = input("Entrez le critère de recherche (téléphone, nom, prénom ou classe) : ").lower()
            valeur = input("Entrez la valeur à rechercher : ")
            # Appel de la fonction de recherche avec les critères spécifiés
            print("\nRésultats de la recherche :")
            # Affichage des résultats de la recherche
            rechercher_etudiant_critere("donnees_etudiants.txt", credits, valeur)
        elif choix == "4":
            print("------------------------------Résultat du tri par ordre décroissant de la moyenne----------------------------", end="\n")
            trier_etudiants_par_moyenne("donnees_etudiants.txt")
        elif choix == "5":
            modifier_etudiant("donnees_etudiants.txt")
            print("------------------------------------Listes des étudiants modifiée--------------------------------------------",end="\n")
        elif choix == "6":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

#Fonction qui se chargera de la recherche de l'étudiant à partir d'un critère
"""def rechercher_etudiant_critere(nom_fichier, critere, valeur):
    
    Fonction pour rechercher un étudiant en fonction d'un critère spécifié.
    
    Args:
        critere (str): Le critère de recherche (téléphone, nom, prénom ou classe).
        valeur (str): La valeur à rechercher.
        
    Returns:
        list: Une liste contenant les informations des étudiants correspondant au critère de recherche.
    
    # Création d'une liste pour stocker les informations des étudiants
    etudiants_recherche = []
    # Lecture du fichier et ajout des informations des étudiants à la liste
    with open(nom_fichier, "r") as fichier:
        for ligne in fichier:
            if critere =="""

def trier_etudiants_par_moyenne(nom_fichier):
    # Création d'une liste pour stocker les informations des étudiants
    etudiants_tries = []

    # Lecture du fichier et ajout des informations des étudiants à la liste
    with open(nom_fichier, "r") as fichier:
        for ligne in fichier:
            prenom, nom, classe, telephone, devoir, projet, examen, moyenne = ligne.strip().split("|")
            etudiants_tries.append((prenom, nom, classe, telephone, float(devoir), float(projet), float(examen), float(moyenne)))

    # Tri des étudiants par moyenne décroissante
    for i in range(len(etudiants_tries)):
        for j in range(i+1, len(etudiants_tries)):
            if etudiants_tries[i][-1] < etudiants_tries[j][-1]:  # Comparaison des moyennes
                etudiants_tries[i], etudiants_tries[j] = etudiants_tries[j], etudiants_tries[i]  # Échange des étudiants

    # Affichage des étudiants triés
    print("\nListe des étudiants triée par moyenne décroissante :", end="\n")
    print()
    print("-"*110)
    print(f"{'Nom':<15} | {'Prénom':<10}  | {'Classe':<10}  | {'Téléphone':<10} | {'Devoir':<10} | {'Projet':<10} | {'Examen':<10} | {'Moyenne':<10} |")
    print("-"*110)
    for etudiant in etudiants_tries:
        prenom, nom, classe, telephone, devoir, projet, examen, moyenne = etudiant
        print(f"{nom:<15} | {prenom:<10}  | {classe:<10}  | {telephone:<10} | {devoir:<10.2f} | {projet:<10.2f} | {examen:<10.2f} | {moyenne:<10.2f} |")
        print("-"*110)

#Fonction pour modifier
def modifier_etudiant(nom_fichier):
    """
    Fonction pour accéder au fichier afin de modifier le contenu sur une ligne.
    Nous allons pour cela utiliser la fonction de recherche en donnant comme critère le numéro de téléphone.
    """
    # L'utilisateur devra saisir le numéro de téléphone de l'étudiant dont il veut modifier les informations.
    critere = "telephone"
    valeur = input("Donner le numéro de téléphone de l'étudiant: ")
    with open(nom_fichier, "r+") as fichier:
        lignes = fichier.readlines()
        fichier.seek(0)
        # Parcourir chaque ligne du fichier
        for ligne in lignes:
            # Vérifier si la valeur du critère spécifié correspond à la valeur recherchée
            infos = ligne.strip().split("|")
            if critere == "telephone" and valeur == infos[3]:
                nom = input("Nom : ")
                prenom = input("Prénom : ")
                classe = input("Classe : ")
                
                # Vérifier que le numéro de téléphone est correct avant d'appeler la fonction number.
                telephone_valide = False
                while not telephone_valide:
                    telephone = input("Téléphone : ")
                    telephone_valide = number(telephone)
                    if not telephone_valide:
                        print("Numéro de téléphone incorrect. Veuillez réessayer.")
                
                devoir = valider_note(input("Note de devoir : "))
                projet = valider_note(input("Note de projet : "))
                examen = valider_note(input("Note d'examen : "))
                moyenne = round((float(devoir) + float(projet) + float(examen)) / 3, 2)

                # Écrire les nouvelles informations des étudiants
                infos[0] = nom
                infos[1] = prenom
                infos[2] = classe
                infos[3] = telephone
                infos[4] = devoir
                infos[5] = projet
                infos[6] = examen
                infos[7] = str(moyenne)

                # Réécrire la ligne dans le fichier
                fichier.writelines('|'.join(str(infos)) + '\n')
            else:
                print("La référence n'existe pas")