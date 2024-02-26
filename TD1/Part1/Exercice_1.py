#Afficher un message demandant à l'utilisateur de saisir deux nombres
#Et l'affecter à une valeur
#Obliger l'utilisateur à saisir des entiers
# Demander la saisie de a
a = int(input("Saisissez a : "))

# Demander la saisie de b
b = int(input("Saisissez b : "))

# Calculer le quotient entier
q_entier = a // b

# Calculer le reste
reste = a % b

# Calculer le quotient réel  
ratio = a / b

# Afficher les résultats
print("Quotient entier :", q_entier)
print("Reste :", reste)
print("Ratio :", ratio)
print("Modulo :", a%b)
