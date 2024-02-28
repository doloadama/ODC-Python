#Demander de donner le nombre de phrases
while True:
    N = input("Donner le nombre de phrases à saisir \n> ")
    if N.isdigit() and int(N) > 0:
        break
    else:
        print("Donnez un nombre correcte!!!!")
N = int(N)
#Initialisations
speciaux = "#$%&/()"

#Recevoir les phrases
while True:
    phrases = input("Entrez une phrase \n > ")
    #Vérification de la majuscule et du point
    if phrases[0].islower() or phrases[-1] != ".":
        print("phrase incorrecte")
    #Vérification des caractères spéciaux
    for i in range(len(speciaux) - 1):
        for j in range(len(phrases)-1):
            if speciaux[i] == phrases[j]:
                print("La phrase n'est pas correct")
            else:
                continue
    #Suppression de l'espace
    for i in range(len(phrases)-1):
    #Si deux espaces se suivent
        if phrases[i] == " " and phrases[i + 1]== " ":
            # Supprimer l'espace en trop
            phrases = phrases[:i] + phrases[i + 1:]
