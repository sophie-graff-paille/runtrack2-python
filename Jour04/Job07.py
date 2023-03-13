L = [8, 24, 48, 2, 16] # liste de 5 éléments
compte = 0 # compteur initialisé à 0
for i in L: # pour chaque élément de la liste L
    if i % 3 == 0: # si le reste de la division de i par 3 est égal à 0
        compte += 1 # incrémentation du compteur

print(compte)