#Demander de donner une phrase
phrase = input("Ecrivez une phrase: ")

#Parcourir la chaine
for i in range(len(phrase)-1):
    #Si deux espaces se suivent
    if phrase[i] == " " and phrase[i + 1]== " ":
         # Supprimer l'espace en trop
        phrase = phrase[:i] + phrase[i + 1:]

print(phrase)
