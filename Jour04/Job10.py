L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91] # liste de 11 éléments
produit = 1 # produit initialisé à 1
for i in L: # pour chaque élément de la liste L
    if i >= 25 and i <= 90: # si l'élément est compris entre 25 et 90
        produit *= i # incrémentation du produit
print(produit)