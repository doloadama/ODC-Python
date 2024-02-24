# Afficher un message demandant à l'utilisateur de saisir une somme
valeur = input("Entrez une valeur en euros : ")

# Vérifier que la valeur est un nombre entier
while not valeur.isdigit():
  print("Erreur : vous devez entrer un nombre entier.")
  valeur = input("Veuillez réessayer : ")

valeur = int(valeur) 

# Taux de change
dollar = 1.05
livre_Sterling = 0.86

# Calculer les equivalents 
val_dollar = valeur * dollar
val_livre = valeur * livre_Sterling

# Afficher les résultats
print(valeur, "euros équivaut à :", round(val_dollar, 2), "dollars")
print(valeur, "euros équivaut à :", round(val_livre, 2), "livres sterling")
