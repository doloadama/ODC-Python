#Demander de donner le nombre de phrases
while True:
    N = input("Donner le nombre de phrases à saisir \n> ")
    if N.isdigit() and int(N) > 0:
        break
    else:
        print("Donnez un nombre correcte!!!!")
N = int(N)

#Initialisations
speciaux = "#$%&/()@+-×÷"; k = False ; phraseN = ""

#Recevoir les phrases
for un in range(N):

    phrases = input("Entrez une phrase \n > ")

    #Vérification de la majuscule et du point
    while True:
        if not phrases[0].isupper() or phrases[-1] != ".":
            print("Une phrase commence par une lettre majuscule et se termine par un point.")
            phrases = input("Entrez une phrase \n > ")
        else:
            break 
    
    #Suppression de l'espace
        for caractere in speciaux:
            if caractere in phrases:
                print("La phrase ne doit pas contenir de caractères spéciaux.", end=" \n")
                phrases = input("Entrez une phrase \n > ")
            else:
                break

    while True:
        if len(phrases) < 25:
            print("La phrase doit avoir au moins 25 caractères")
            input("Entrez une phrase \n > ")
        else:
            break
    
    #Suppression espacements
    for i in phrases:
        if i == " " and  k:
            continue
        else:
            phraseN += i
            k = (i == " ") #mets à jour k en vérifiant si i == " " et met true
print(phraseN)
