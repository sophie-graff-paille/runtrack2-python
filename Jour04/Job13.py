L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40] # liste de 11 éléments
new_L = [] # liste vide

for i in L: # pour chaque élément de la liste L
    if i not in new_L: # si l'élément n'est pas dans la liste new_L
        new_L += [i] # ajout de l'élément à la liste new_L
print(new_L)