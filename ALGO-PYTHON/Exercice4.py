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
    numb = numb.strip()
    debutNumero = numb[:2]
    
    #Vérifier les deux premiers digits
    # Vérifier les deux premiers chiffres
    if debutNumero in commence and len(numb.replace(" ", "")) == 9:
        valide += numb
        print("Numéro correct")
    else:
        invalide += numb
        print("Numéro incorrect")

# Afficher les numéros valides à gauche et les numéros invalides à droite
print("\nNuméros valides :\t\t\tNuméros invalides :")
for val, inval in zip(valide, invalide):
    print(f"{val:25}\t\t\t{inval:25}")
