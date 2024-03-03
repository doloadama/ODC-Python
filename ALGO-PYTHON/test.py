# Définition de la classe Etudiant
class Etudiant:
    def __init__(self, nom, prenom, classe, tel, note_devoir, note_projet, note_examen):
        self.nom = nom
        self.prenom = prenom
        self.classe = classe
        self.tel = tel
        self.note_devoir = note_devoir
        self.note_projet = note_projet
        self.note_examen = note_examen

# Initialisation de la liste d'étudiants
etudiants = []

def saisie_etudiant():
    nom = input("Nom de l'étudiant : ")
    prenom = input("Prénom de l'étudiant : ")
    classe = input("Classe de l'étudiant : ")
    tel = input("Numéro de téléphone de l'étudiant : ")
    note_devoir = float(input("Note de devoir : "))
    note_projet = float(input("Note de projet : "))
    note_examen = float(input("Note d'examen : "))
    return Etudiant(nom, prenom, classe, tel, note_devoir, note_projet, note_examen)

def calcul_moyenne(etudiant):
    return (etudiant.note_devoir + etudiant.note_projet + etudiant.note_examen) / 3

def afficher_etudiants():
    print("\nListe des étudiants :")
    print("{:<15} {:<15} {:<10} {:<15} {:<10}".format("Nom", "Prénom", "Classe", "Téléphone", "Moyenne"))
    for etudiant in etudiants:
        moyenne = calcul_moyenne(etudiant)
        print("{:<15} {:<15} {:<10} {:<15} {:<10.2f}".format(etudiant.nom, etudiant.prenom, etudiant.classe, etudiant.tel, moyenne))

def trier_etudiants():
    etudiants.sort(key=lambda x: calcul_moyenne(x), reverse=True)

def rechercher_etudiant(critere):
    for etudiant in etudiants:
        if critere.lower() in (etudiant.nom.lower(), etudiant.prenom.lower(), etudiant.classe.lower(), etudiant.tel.lower()):
            return etudiant
    return None

def modifier_notes():
    tel = input("Entrez le numéro de téléphone de l'étudiant dont vous souhaitez modifier les notes : ")
    etudiant = rechercher_etudiant(tel)
    if etudiant:
        etudiant.note_devoir = float(input("Nouvelle note de devoir : "))
        etudiant.note_projet = float(input("Nouvelle note de projet : "))
        etudiant.note_examen = float(input("Nouvelle note d'examen : "))
        print("Notes mises à jour avec succès !")
    else:
        print("Étudiant introuvable.")

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
            print(f"Nom : {etudiant.nom}, Prénom : {etudiant.prenom}, Classe : {etudiant.classe}, Téléphone : {etudiant.tel}")
        else:
            print("Aucun étudiant trouvé.")
    elif choix == "5":
        modifier_notes()
    elif choix == "6":
        print("Merci d'avoir utilisé notre application !")
        break
    else:
        print("Option invalide. Veuillez réessayer.")
