#Affichage d'un message de bienvenue
print("-----------------------------------*Bienvenue dans votre clavier*---------------------------------")

#Demander à l'utilisateur d'écrire
valeur = input("Commencez la saisie\n >")
valeur = str(valeur)

#Création d'une variable d'affichage

#Création d'une fonction gérant les entrées texte
def lettrem(phrase):
    #Dictionnaires contenant les références en majuscules
    lettres = {
    "2": "A", "22": "B", "222": "C", "3": "D",
    "33": "E", "333": "F", "4": "G", "44": "H",
    "444": "I", "5": "J", "55": "K", "555": "L",
    "6": "M", "66": "N", "666": "O", "7": "P",
    "77": "Q", "777": "R", "7777": "S", "8": "T",
    "88": "U", "888": "V", "9": "W", "99": "X",
    "999": "Y", "9999": "Z", "0": " "
}

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
                  "*": "*", "#": "#"
                 }

    #Une boucle pour vérifier la correspondance dans les différents dictionnaires
    traduction = ''
    succession = ''
    for carac in phrase.upper():
        #variable qui prend chaque valeur afin de comparer au suivant
        code = ''
        if carac in lettres:
            code += lettres[carac]
        elif carac in chiffres:
            code += chiffres[carac]
        elif carac in caracteres:
            code += caracteres[carac]
        else:
            code = "0"
    
        if code == succession:
            traduction += "0" + code
        else:
            traduction += code
        
        succession = code

    return traduction


#Création d'une variable prenant la phrase entrée
phrase = valeur

#Appel de la fonction de traduction et traduction de la phrase
traduction  = lettrem(phrase)

#Affichage de la phrase traduite
print()
print("--------------------Voici votre traduction------------------------")
print()
print("\t \t   ",traduction)
