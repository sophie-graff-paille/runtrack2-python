# fonction qui prend en paramètre une liste de nombres et qui renvoie la longueur de la liste
def length(L):
    total = 0 # total initialisé à 0
    for i in L: # pour chaque élément de la liste L
        total += 1 # incrémentation du total
    return total

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
print(length(L))
 # fonction qui prend en paramètre une liste de nombres et qui renvoie une liste contenant les nombres de la liste d'origine triés par ordre croissant
def croissant(L):
    i = 0 # indice initialisé à 0
    for i in range(length(L)): # pour chaque élément i de la liste L
        for j in range(i+1, length(L)): # pour chaque élément j de la liste L
            if L[i] > L[j]: # si l'élément i est supérieur à l'élément j
                L[i], L[j] = L[j], L[i] # échange des éléments i et j
    return L
print(croissant(L))