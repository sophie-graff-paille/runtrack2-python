# fonction qui affiche les nombres de 1 à 100 exceptés 26, 37 et 88
def affichenb3():
    i = 0
    for i in range(100):
        if i != 26 and i != 37 and i != 88:
            print(i)

affichenb3()