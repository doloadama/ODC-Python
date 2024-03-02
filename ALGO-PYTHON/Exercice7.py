
#Dictionnaires contenant les références numériques
chiffres = {
            "A": "0", "B": "1",
            "C": "2", "D": "3",
            "E": "4", "F": "5",
            "G": "6", "H": "7", 
            "I": "8", "J": "9"
            }

#Dictionnaires contenant les références de caractères spéciaux et espace
caracteres = {
             " ": "00", "*": "*", "#": "#"
             }

#Affichage d'un message de bienvenue
print("-----------------------------------*Bienvenue dans votre clavier*---------------------------------")

#Demander à l'utilisateur d'écrire
valeur = input("Commencez la saisie\n >")
valeur = str(valeur)

#Création d'une variable d'affichage

#Création d'une fonction gérant les entrées texte
def lettrem(phrase):
    #Dictionnaires contenant les références en majuscules
    correspondance = {
            "A": "2",
            "B": "22", "C": "222", "D": "3", 
            "E": "33", "F": "333", "G": "4", 
            "H": "44", "I": "444", "J": "5",
            "K": "55", "L": "555", "M": "6",
            "N": "66", "O": "666", "P": "7",
            "Q": "77", "R": "777", "S": "7777",
            "T": "8",  "U": "88",  "V": "888",
            "W": "9",  "X": "99",  "Y": "999",
            "Z": "9999", " ": "0" 
            }

    traduction = ''
    for lettre in phrase.upper():
        if lettre in correspondance:
            traduction += correspondance[lettre]
    
    return traduction


phrase = valeur
traduction  = lettrem((phrase))
print(traduction)


#Création d'une fonction gérant les chiffres
    





#Création d'une fonction gérant les caractères spéciaux




