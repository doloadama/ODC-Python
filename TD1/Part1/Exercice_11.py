# Afficher un message demandant les données du produit
libelle = str(input("Donnez les libelé du produit: "))
quantite_stock = float(input("Veuillez donner la quantité en stock du produit: "))
prix_unitaire = float(input("Veuillez saisir le prix unitaire du produit: "))

# Calculer le montant en stock
MStock = prix_unitaire * quantite_stock

# Calculer le montant TTC
TVA = 0.18  # TVA de 18%
MTTC = MStock + MStock * TVA

# Afficher les informations du produit
print("Libellé du produit :", libelle)
print("Quantité en stock :", quantite_stock)
print("Prix unitaire :", prix_unitaire)
print("Montant en stock :", MStock)
print("Montant TTC :", MTTC)
