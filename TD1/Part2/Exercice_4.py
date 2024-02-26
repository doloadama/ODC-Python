#Afficher un message demandant de donner une somme
#Verifier que l'entrée est positive et est un entier
while True:
    argent = input("Veuillez entrez une somme: ")
    if argent.isdigit():
        break
    else:
        print("Veuillez saisir un montant correct!")

argent = int(argent)

#Initialiser les variables representant la monnaie 
twenty= 0; ten = 0; five = 0; two = 0; one_piece = 0

#décompte du nombre de billets de 20
while argent >= 20:
    twenty += 1
    argent -=  20

#décompte du nombre de billets de 10
while argent >= 10:
    ten += 1
    argent -= 10

#décompte du nombre de billets de 5
while argent >= 5:
    five += 1
    argent -= 5

#décompte du nombre de pièces de 2
while argent >= 2:
    two += 1
    argent -= 2

#décompte du nombre de pièces de 5
while argent >= 1:
    one_piece += 1
    argent -= 1

print("la monnaie est de : ", twenty, "billets de 20 \n", ten, " billets de 10\n"
      , five, " billets de 5\n", two, " pièces de 2\n", one_piece, " pièces de 1")

