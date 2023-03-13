# boucle while qui permet d'afficher à l'envers une chaîne de caractères saisie par l'utilisateur
chaîne = input("Entrez une chaîne de caractères: ")
inverse = ""
i = len(chaîne)
while i > 0:
    inverse += chaîne[i-1]
    i -= 1
print(inverse)