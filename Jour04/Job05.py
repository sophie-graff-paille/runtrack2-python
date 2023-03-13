L = [2, 6, 13, 86, 8] # liste de 5 chiffres
print(L[1])

def remplace(): # fonction qui remplace le 2ème chiffre de la liste par la somme des 3ème et 5ème chiffres
    L[3] = L[2] + L[4]
    print(L[4])

remplace()