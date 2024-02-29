#Initialisation
commence = ["77","78","76","70","75"] #Contient les dépendances de début de numérp


#Demander de donner une phrase
def sans_espace(phrases):

    phraseN = ""
    #Parcourir la chaine
    for i in phrases:
            if i == " ":
                continue
            else:
                phraseN += i
    return (phraseN)

phrases = " Je dshjgqsdfjhdkfjfd     dsjhsdhdsjksd    dqdkjdskjsdkj"
print(sans_espace(phrases))

#Saisir le nombre de numéro

while True:
     num = input("Saisir le nombre de numéros à donner\n> ")
     if num.isdigit() and int(num) > 0:
          break
     else:
          print("Nombre incorrecte")

for i in range(num):
    number = input("Saisir le numéro")
    num = sans_espace(num)
    debut = number[:2]

    if debut in commence and len(number) == 9:
         print("correct")
