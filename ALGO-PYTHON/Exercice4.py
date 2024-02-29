#Demander de donner le nombre de phrases
while True:
    N = input("Donner le nombre de numéros à saisir \n> ")
    if N.isdigit() and int(N) > 0:
        break
    else:
        print("Donnez un nombre correcte!!!!")
N = int(N)

#Initialisation
commence = ["77","78","76","70","75"] #Contient les dépendances de début de numérp
valide = "" #Récupère les numéros valide
invalide = "" #Recupère les numéros invalides
taille = 0 #Recupère la taille du numéro aprés retrait ou non des espaces

#Saisie des numéros
for i in range(N):
    numb = input("Saisir un numéro: \n>")
    debutNuméro = numb[:1]

    #Vérifier les deux premiers digits
    if debutNuméro in commence:
        valide += numb
        print("Numéro correct")
    else:
        invalide += numb
        print("Numéro incorrect")

    #Verifier la longueur du numéro
    for j in range(len(numb)):
            #Pour chaque espace 
            if " " in numb:
                taille = len(numb) - 1
                continue
    #veirfier si la taille après retrait des espaces est de 9
    if taille == 9:
        valide += numb
        print(f"{valide:10}", end = "\t")
        print()
    else:
        invalide += numb
        print(f"{invalide:10}", end = "\t")
        print()
