#Demander un nombre à l'utilisateur
#Verifier que ce nombre est non nul et est un entier
while True:
    nombre = input("Veuillez fournir un nombre entier: ")
    if nombre.isdigit() > 0:
        break
    else:
        print("Le nombre n'est pas valide!")
nombre = int(nombre)

#Initialisations des variables
parfait = 0; i = 0

#Recherche des diviseurs
for i in range(1, nombre - 1):
    if nombre % i == 0:
        parfait += i

#Comparaison de la somme et du nombre et affaihage du résultat
if parfait == nombre:
    print("Le nombre est parfait, la somme des diviseurs est : ", parfait)
else:
    print("Le nompbre n'est pas parfait, la somme des diviseurs est : ", parfait)
