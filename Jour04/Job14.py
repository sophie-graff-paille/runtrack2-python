def length(L):
    total = 0
    for i in L:
        total += 1
    return total

L = "Demain dès l'aube à l'heure où blanchit la campagne je partirai je ne puis demeurer loin de toi plus longtemps"

def recherche_longueur_mot(L, longueur):
    mot = ""
    motspluslongs = ""
    for i in range(length(L)):
        if L[i] == " " or i == length(L)-1:
            if i == length(L)-1 and L[i] != " ":
                mot += L[i]
            if length(mot) > longueur:
                motspluslongs += mot + " "
            mot = ""
        else:
            mot += L[i]
    return motspluslongs

print(recherche_longueur_mot(L, 6))
