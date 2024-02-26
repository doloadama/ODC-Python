#Demander un nombre a
#Vérifier que ce nombre est positif
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
    elif a > b:
        break
    else:
        print("Le nombre n'est pas correct")
b = int(b)

#Initialisation des varibles
ppcm = 0; pgcd = 0

#Recherche du PGCD
while a != b:
    if a > b:
      a -= b
    else:
      b -= a
    pgcd = a

ppcm = (a * b) // pgcd


#Affichage du résultat
print("Le PPCM de ", a, " et ", b , " est : ",ppcm)
