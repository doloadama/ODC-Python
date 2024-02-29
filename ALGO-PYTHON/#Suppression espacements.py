    #Suppression espacements
k=False
for i in phrases:
            if i == " " and  k:
                continue
            else:
                phraseN += i
                k = (i == " ") #mets à jour k en vérifiant si i == " " et met true
print(phraseN, end="\n")