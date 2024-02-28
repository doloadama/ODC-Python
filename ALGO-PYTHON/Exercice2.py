#Demander de donner une phrase
phrases = input("Ecrivez une phrase: ")
phraseN = ""

#Parcourir la chaine
for i in phrases:
        if i == " " and  k:
            continue
        else:
            phraseN += i
            k = (i == " ") #mets à jour k en vérifiant si i == " " et met true

print(phrases)
