#Afficher un message demandnant à l'utilisateur de saisir des nombres
#Verifier si l'entrée sont des nombres
mesure = int(input("Veuillez donner une mesure en dm: "))

#Convertir en m
metre = mesure // 10
#Convertir en mm
millimetre = mesure * 100
#Convertir en cm
centimetre = mesure * 10
#Convertir en hm
hectometre = mesure // 1000

#Afficher les resultats de conversion
print("la conversion en mètre est de : ", metre,"mètre")
print("la conversion en millimetre est de : ", millimetre,"millimètre")
print("la conversion en mètre est de : ", centimetre,"centimètre")
print("la conversion en mètre est de : ", hectometre,"hectomètre")
