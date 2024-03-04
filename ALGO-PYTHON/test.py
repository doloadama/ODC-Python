#Demander à l'utilisateur de donner le nombre de numéros qu'il veut saisir
while True:
    nombre = input("nombre: ")
    if nombre.isdigit() and int(nombre) > 0:
        break
    else:
        print("Nombre invalide, veuillez reessayer")

nombre  = int(nombre)

liste_debut_num  = ["77", "76", "75", "70", "78"]
valide = []
invalide = []

#Saisir et contrôler les numéros que l'utilisateur va saisir
for i in range(nombre):
    #Saisir le numéro
    numero = input("Saisir un numéro: ")
    #Supprimer les espaces en début de numéro
    numero.strip()
    #Recuperer les deux premiers caractères du numéro saisi
    debut = numero[0:2]

    #comparaison des deux premiers caractères du numéro saisi avec le contenu de la liste
    if debut in liste_debut_num and len(numero.replace(" ", "")) == 9:
        valide.append(numero)
        print("numéro valide", end="\n")
    else:
        invalide.append(numero)
        print("numero invalide", end="\n")

for i in range(len(valide)):
    print("Numeros valides \t \t numeros invalides")
    print(f"{valide[i]:14} \t \t \t {invalide[i]:17}")
