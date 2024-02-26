#Demander un nombre
#Demander de saisir un nombre
##érifier que ce nombre est positif
while True:
    a = input("Veuillez fournir un nombre entier: ")
    if a.isdigit() > 0:
        break
    else:
        print("Le nombre n'est pas valide!")
a = int(a)

#Inititialisation
i = 0; div = 0
#Verifier si le nombre a des diviseurs
for i in range(2, a-1):
    if a % i == 0:
        div += i
        
if div  == a :
    print(f"le nombre {a} parfait")
else:
    print(f"le nombre {a} n'est pas parfait")
