# fonction qui calcule la longueur d'une liste
def length(L):
    total = 0 # total initialisé à 0
    for i in L: # pour chaque élément de la liste L
        total += 1 # incrémentation du total
    return total

L = "Demain dès l'aube à l'heure où blanchit la campagne je partirai je ne puis demeurer loin de toi plus longtemps"

# fonction qui recherche les mots d'une longueur donnée
def recherche_longueur_mot(L, longueur): 
    mot = "" # mot initialisé à une chaîne vide
    motspluslongs = "" # motspluslongs initialisé à une chaîne vide
    for i in range(length(L)): # pour chaque élément i de la liste L
        if L[i] == " " or i == length(L)-1: # si i est un espace ou si i est égal à la longueur de la liste L moins 1
            if i == length(L)-1 and L[i] != " ": #
                mot += L[i] # ajout de l'élément i à la chaîne mot
            if length(mot) > longueur: # si la longueur du mot est supérieure à la longueur donnée
                motspluslongs += mot + " " # ajout du mot à la chaîne motspluslongs
            mot = "" # réinitialisation de la chaîne mot
        else:
            mot += L[i] # ajout de l'élément i à la chaîne mot
    return motspluslongs

print(recherche_longueur_mot(L, 6))
