mot = input("veuiller saisir un mot: ")

liste = ['a','e','i','o','u','y']

compteur = 0

for lettre in mot:

    if lettre in liste:
        print("votre mot comporte",lettre)
        compteur += 1
if compteur == 0 :
    print("Votre mot ne comporte aucune voyelle.")
else:
 print("Bravo ! Votre mot comporte au total", compteur , "voyelles.")
