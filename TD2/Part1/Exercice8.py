#Demander à l'utilisateur de saisir un nombre
while True:
    a = input("Veuillez donner un nombre à deviner ")
    if a.isdigit():
        break
    else:
        print("Nombre incorrect!")
a = int(a)

#Demander de deviner le prmier nombre
b = int(input("Devinez le nombre :) : "))

score = 1

#Verifier si trouvé et recommencer sinon
while a != b:
    print("Oups, dommage!")
    b = int(input("Devinez le nombre :) : "))
    score += 1 

#Afficher 
print("Bravo!!!")
print(score," tentatives")
