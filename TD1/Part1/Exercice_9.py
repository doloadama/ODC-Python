#Afficher un message demandant de donner les temps
heure_depart = int(input("veuillez saisir l'heure de départ: "))
minute_depart = int(input("veuillez saisir l'heure de départ: "))
heure_arrivee = int(input("veuillez saisir l'heure d'arrivée: "))
minute_arrivee = int(input("veuillez saisir l'heure d'arrivée: "))

heures = 0; minutes = 0

# Heure d'arrivée (par exemple, 7h45 le lendemain)
heure_arrivee_h = 7
minute_arrivee_m = 45

# Calculer la durée en heures et minutes
if heure_arrivee >= heure_depart:
    heures = heure_arrivee - heure_depart
    if minute_arrivee_m >= minute_depart:
        minutes = minute_arrivee_m - minute_depart
    else:
        minutes = minute_arrivee_m + 60 - minute_depart
        heures -= 1
else:
    heures = heure_arrivee_h + 24 - heure_depart
    if minute_arrivee_m >= minute_depart:
        minutes = minute_arrivee_m - minute_depart
    else:
        minutes = minute_arrivee_m + 60 - minute_depart
        heures -= 1

#Afficher la duréee du vol
print("Durée du vol : ", heures, "heure(s) et", minutes, "minute(s)")
