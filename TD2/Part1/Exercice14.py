#Demander de saisir un nombre
##érifier que ce nombre est positif
while True:
    N = input("Veuillez fournir un nombre entier: ")
    if N.isdigit() > 0:
        break
    else:
        print("Le nombre n'est pas valide!")
N= int(N)

#Initialisation des variables
i = 0; premier = []

#Vérification des nombres premiers
for i in range(1, N-1):
    if N % i != 0:
        premier.append(i)

print(f"Les nombres premiers compris entre 1 et {N} sont : {premier}")
