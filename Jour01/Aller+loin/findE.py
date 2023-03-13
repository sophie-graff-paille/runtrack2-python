# fonction qui permet de trouver un e dans une chaîne de caractères
def findE():
    chaîne = input("Entrez votre chaîne de caractères : ")
    if "e" in chaîne:
        print("Votre chaîne contient au moins un 'e'")
    else:
        print("Votre chaîne ne contient pas de 'e'")
findE()