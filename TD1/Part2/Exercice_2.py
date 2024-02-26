#Afficher un message demandant de donner un nombre
while True:
    a = input("Choisir le premier entier: ")
    if a.isdigit():
        break
    else:
        print("entrée incorrecte!")

a =int(a)

#Afficher un message deamandant de choisir l'opération
operateur = str(input("choisir l'opération: "))

#Afficher un message demandant de donner un nombre
while True:
    b = input("Choisir le deuxième entier: ")
    if b.isdigit():
        break
    else:
        print("entrée incorrecte!")

b =int(b)

#Si b est inférieur à a et l'opération est une différence
if operateur == "-" and a < b:
        b = input("Choisir le deuxième entier: ")

#Faire le calcul et afficher le resultat
if operateur == "+":
    somme = a + b
    print("a + b = ", somme)

#Faire le calcul et afficher le resultat
if operateur == "+":
    différence = a * b
    print("a - b = ", différence)
