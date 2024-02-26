#Affichage d'un message demandant de donner trois entiers
a= int(input("Donnez A: "))
b = int(input("Donnez B: "))
c = int(input("Donnez C: "))

#Initialisation des variables
first = 0; middle = 0; last = 0

#Verifier l'ordre des nombres
if a < b:
    last = a
    first = b
else:
    last = b
    first = a

if c < last:
    middle = last
    last = c

if c > first:
    middle = first
    first  = c
else:
    middle = c

#Afficher dans l'ordre croissant
print("ordre croissant: ", last, " - ", middle, " - ", first)

#Afficher dans l'ordre décroissant
print("ordre croissant: ", first, " - ", middle, " - ", last)
