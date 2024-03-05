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

#Gestion de la saisie des informations des étudiants
def saisie_etudiant():
    """
    Fonction pour saisir les informations d'un étudiant.
    """
    while True:
        nom = input("Nom de l'étudiant : ")
        prenom = input("Prénom de l'étudiant : ")
        classe = input("Classe de l'étudiant : ")
        telephone = input("Téléphone de l'étudiant : ")
        
        if not number(telephone) and not telephone.isdigit():
            print("Format de numéro incorrect. Veuillez réessayer.")
            continue
        
        devoir = input("Note de devoir : ")
        if not valider_note(devoir):
            print("La note de devoir est incorrecte. Veuillez réessayer.")
            continue
        
        projet = input("Note de projet : ")
        if not valider_note(projet):
            print("La note de projet est incorrecte. Veuillez réessayer.")
            continue
        
        examen = input("Note d'examen : ")
        if not valider_note(examen):
            print("La note d'examen est incorrecte. Veuillez réessayer.")
            continue
        
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
    print("{:<15} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10}".format("Prénom", "Nom", "Classe", "Téléphone", "Devoir", "Projet", "Examen", "Moyenne"))
    print("-" * 110)

    with open("donnees_etudiants.txt", "r") as fichier:
        for ligne in fichier:
            prenom, nom, classe, telephone, devoir, projet, examen, moyenne = ligne.strip().split("|")
            print("{:<15} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10.2}".format(prenom, nom, classe, telephone, devoir, projet, examen, moyenne))
            print("-" * 110)


# Menu principal
def menu():
    """
    Fonction pour afficher le menu principal.
    """
    while True:
        print("\nMenu :")
        print("1. Saisir les informations d'un étudiant")
        print("2. Afficher tous les étudiants")
        print("3. rechercher un étudiant")
        print("4. Rechercher un étudiant (par téléphone, nom, prénom ou classe)")
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
            resultats_recherche = rechercher_etudiant_critere(critere, valeur)
            if resultats_recherche:
                print("\nRésultats de la recherche :")
                for etudiant in resultats_recherche:
                    print(etudiant)  # Affichage des informations de chaque étudiant trouvé
            else:
                print("Aucun résultat trouvé pour la recherche spécifiée.")  # Message si aucun étudiant n'est trouvé
        elif choix == "4":
            trier_par_la_moyenne("donnees_etudiant.txt")
            afficher_etudiants()
        elif choix == "6":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def rechercher_etudiant_critere(critere, valeur):
    """
    Fonction pour rechercher un étudiant en fonction d'un critère spécifié.
    
    Args:
        critere (str): Le critère de recherche (téléphone, nom, prénom ou classe).
        valeur (str): La valeur à rechercher.
        
    Returns:
        list: Une liste contenant les informations des étudiants correspondant au critère de recherche.
    """
    etudiants_trouves = []  # Une liste pour stocker les étudiants trouvés
    
    # Ouvrir le fichier contenant les données des étudiants en mode lecture
    with open("donnees_etudiants.txt", "r") as fichier:
        # Parcourir chaque ligne du fichier
        for ligne in fichier:
            # Extraire les informations de l'étudiant de la ligne et les stocker dans des variables
            prenom, nom, classe, telephone, devoir, projet, examen, moyenne = ligne.strip().split("|")
            # Vérifier si la valeur du critère spécifié correspond à la valeur recherchée
            if critere == "telephone" and valeur == telephone:
                # Si c'est le cas, ajouter les informations de l'étudiant à la liste des étudiants trouvés
                etudiants_trouves.append((prenom, nom, classe, telephone, devoir, projet, examen, moyenne))
            elif critere == "nom" and valeur == nom:
                etudiants_trouves.append((prenom, nom, classe, telephone, devoir, projet, examen, moyenne))
            elif critere == "prenom" and valeur == prenom:
                etudiants_trouves.append((prenom, nom, classe, telephone, devoir, projet, examen, moyenne))
            elif critere == "classe" and valeur == classe:
                etudiants_trouves.append((prenom, nom, classe, telephone, devoir, projet, examen, moyenne))
    
    # Retourner la liste des étudiants trouvés
    return etudiants_trouves

def affichage_recherche():
    # Appel de la fonction de recherche avec les critères spécifiés

    # Affichage des résultats de la recherche
    if rechercher_etudiant_critere():
        print("\nRésultats de la recherche :")
        for etudiant in rechercher_etudiant_critere:
            print(etudiant)  # Affichage des informations de chaque étudiant trouvé
    else:
        print("Aucun résultat trouvé pour la recherche spécifiée.")  # Message si aucun étudiant n'est trouvé

def trier_par_la_moyenne(nom_fichier):
    """
    Fonction pour trier les lignes d'un fichier selon la moyenne des étudiants.

    Args:
        nom_fichier (str): Le nom du fichier à trier.

    Returns:
        None
    """

    # Lire les données du fichier
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()

    # Trier les lignes selon le critère de tri
    lignes_triees = sorted(lignes, key=lambda ligne: float(ligne.split('|')[-1]))

    # Écrire les lignes triées dans le fichier
    with open(nom_fichier, 'w') as fichier:
        fichier.writelines(lignes_triees)
