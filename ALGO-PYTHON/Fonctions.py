def numero(numb):
    # Gestion des numéros de téléphone valides
    commence = {"77", "78", "76", "70", "75"}  # Contient les dépendances de début de numéro

    # Supprimer les espaces inutiles dans le numéro
    numb = numb.replace(" ", "")

    # Vérifier si la longueur du numéro est correcte
    if len(numb) == 9:
        # Extraire les deux premiers chiffres du numéro
        debutNumero = numb[:2]
        # Vérifier si les deux premiers chiffres sont valides
        if debutNumero in commence:
            # Retourner le numéro valide
            return numb
        else:
            # Retourner un message d'erreur si les deux premiers chiffres ne sont pas valides
            return "Numéro incorrect: les deux premiers chiffres ne sont pas valides"
    else:
        # Retourner un message d'erreur si la longueur du numéro est incorrecte
        return "Numéro incorrect: la longueur du numéro doit être de 9 chiffres"
#--------------------------------------------------------------------------------------------------------
#Création étudiant
def saisir_info_etudiant():
    etudiant = {}
    prenom = input("Entrez le prénom de l'étudiant: ")
    nom = input("Entrez le nom de l'étudiant: ")
    telephone = input("Entrez le numéro de téléphone de l'étudiant: ")
    telephone = numero(telephone)
    classe = input("Entrez la classe de l'étudiant: ")

    #Contrôle de la saisie de la note de devoir
    while True:
        note_devoir = (input("Entrez la note de devoir de l'étudiant (entre 0 et 20): "))
        if note_devoir.isdigit() and 0 <= note_devoir <= 20:
            break
        else:
            print("La note doit être un chiffre et comprise entre 0 et 20, veuillez reessayer")
    note_devoir = float(note_devoir)

    #Contrôle de la saisie de la note de projet
    while True:
        note_projet = (input("Entrez la note de projet de l'étudiant (entre 0 et 20): "))
        if note_projet.isdigit() and 0 <= note_projet <= 20:
            break
        else:
            print("La note doit être un chiffre et comprise entre 0 et 20, veuillez reessayer")
    note_projet = float(note_projet)

    #Contrôle de la saisie de la note d'examen
    while True:
        note_examen = (input("Entrez la note d'examen de l'étudiant (entre 0 et 20): "))
        if note_examen.isdigit() and 0 <= note_examen <= 20:
            break
        else:
            print("La note doit être un chiffre, veuillez reessayer")
    note_examen = float(note_examen)
    
    etudiant = {"prenom":prenom, "nom":nom, "telephone":telephone, "classe":classe,
                    "note_devoir":note_devoir, "note_projet":note_projet, "note-exam":note_examen}

