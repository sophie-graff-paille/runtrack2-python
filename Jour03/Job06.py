# fonction qui prend en variable une chaîne de caractères
# et qui affiche une pyramide à partir de cette chaîne * 10
def pyramide():
    chaîne = "abcdefghijklmnopqrstuvwxyz" * 10
    p = ""
    for i in chaîne:
        p += i
        print(p)

pyramide()