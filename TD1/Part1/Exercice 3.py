#Afficher un message demandnant à l'utilisateur de saisir des nombres

celsius = int(input("Veuillez donner une teméparture en degré Celsius: "))

"""while not isinstance(celsius, int):
    print("la donnée doit être un entier")
    celsius = input("Saisissez à nouveau la température: ")
celsius = int(celsius)
"""
#Convertir degré en Fahrenheit
fahrenheit = (celsius * 9/5) + 32

#Afficher la valeur de la conversion
print(celsius, "degrés Celsius = ", fahrenheit, "degrés Fahrenheit")
