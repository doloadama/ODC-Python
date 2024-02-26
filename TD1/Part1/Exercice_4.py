# Importer le module math où est stocké la valeur de Pie
import math

# Demander le rayon 
rayon = float(input("Entrez le rayon du cercle : "))

# Calcul du périmètre 
perimetre = 2 * math.pi * rayon

# Calcul de la surface
surface = math.pi * rayon ** 2

# Afficher les résultats
print("Périmètre du cercle :", int(round(perimetre, 2))) 
print("Surface du cercle :", int(round(surface, 2)))
