#Demander de saisir un nombre
##érifier que ce nombre est positif
while True:
    a = input("Veuillez fournir un nombre entier: ")
    if a.isdigit() > 0:
        break
    else:
        print("Le nombre n'est pas valide!")
a = int(a)

#Demander un nombre b
#Vérifier que ce nombre est positif
while True:
    b = input("Veuillez fournir un nombre entier: ")
    if b.isdigit() > 0 :
        break
    else:
        print("Le nombre n'est pas correct")
b = int(b)

#Initialisation
sommeA = 0; sommeB = 0

#calcul de la somme des diviseurs de a
for i  in range (2, a-1):
    if a % i == 0:
        sommeA += i

#calcul de la somme des diviseurs de b
for i  in range (2, b-1):
    if b % i == 0:
        sommeB += i

#Comparer les sommes et afficher le résultat
if sommeA == sommeB:
    print(f"{a} et {b} sont amis")
else:
    print(f"{a} et {b} ne sont pas amis")
