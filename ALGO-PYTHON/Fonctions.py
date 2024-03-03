etudiants = []

#Création d'une fonction devant gérer la saisie des informations d'un étudiant
def saisie_etudiant():
    nom = input("Nom de l'étudiant : ")
    prenom = input("Prénom de l'étudiant : ")
    classe = input("Classe de l'étudiant : ")
    tel = input("Numéro de téléphone de l'étudiant : ")
    while True:
        note_devoir = (input("Note de devoir : "))
        if note_devoir.isdigit() and 0 <= note_devoir <= 20:
            break
        else:
            print("La note est incorrecte, veuillez reessayer")
    note_devoir = float(note_devoir)
    while True:
        note_projet= (input("Note de projet : "))
        if note_projet.isdigit() and 0 <= note_projet <= 20:
            break
        else:
            print("La note est incorrecte, veuillez reessayer")
    note_projet = float(note_projet)
    while True:
        note_examen = (input("Note d'examen : "))
        if note_examen.isdigit() and 0 <= note_examen <= 20:
            break
        else:
            print("La note est incorrecte, veuillez reessayer")
    note_examen = float(note_examen)

    return {
        "nom": nom,
        "prenom": prenom,
        "classe": classe,
        "tel": tel,
        "note_devoir": note_devoir,
        "note_projet": note_projet,
        "note_examen": note_examen
    }


def calcul_moyenne(etudiant):
    return (etudiant["note_devoir"] + etudiant["note_projet"] + etudiant["note_examen"]) / 3

def afficher_etudiants():
    print("\nListe des étudiants :")
    print("{:<15} {:<15} {:<10} {:<15} {:<10}".format("Nom", "Prénom", "Classe", "Téléphone", "Moyenne"))
    for etudiant in etudiants:
        moyenne = calcul_moyenne(etudiant)
        print("{:<15} {:<15} {:<10} {:<15} {:<10.2f}".format(etudiant["nom"], etudiant["prenom"], etudiant["classe"], etudiant["tel"], moyenne))

def trier_etudiants():
    etudiants.sort(key=lambda x: calcul_moyenne(x), reverse=True)

def rechercher_etudiant(critere):
    for etudiant in etudiants:
        if critere.lower() in (etudiant["nom"].lower(), etudiant["prenom"].lower(), etudiant["classe"].lower(), etudiant["tel"].lower()):
            return etudiant
    return None

def modifier_notes():
    tel = input("Entrez le numéro de téléphone de l'étudiant dont vous souhaitez modifier les notes : ")
    etudiant = rechercher_etudiant(tel)
    if etudiant:
        etudiant["note_devoir"] = float(input("Nouvelle note de devoir : "))
        etudiant["note_projet"] = float(input("Nouvelle note de projet : "))
        etudiant["note_examen"] = float(input("Nouvelle note d'examen : "))
        print("Notes mises à jour avec succès !")
    else:
        print("Étudiant introuvable.")