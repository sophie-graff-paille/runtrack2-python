# fonction qui prend un nombre en paramètre et qui affiche si ce nombre est positif, négatif ou nul
def Posneg(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("nul")

Posneg(3)
Posneg(-8)
Posneg(0)
Posneg(15)