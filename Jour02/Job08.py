# fonction qui prend en paramètre un type de produit et une saison
# et qui renvoie un panier de fruits ou légumes en fonction de la saison
def Panier(type, saison):
    if type == "fruits" and saison == "hiver":
        return "orange, mandarine et kiwi"
    elif type == "fruits" and saison == "été":
        return "poire, fraise et cassis"
    elif type == "légumes" and saison == "hiver":
        return "carotte, topinambour et endive"
    elif type == "légumes" and saison == "été":
        return "artichaut, aubergine et navet"
    else:
        return "Je ne connais pas ce produit"
    
print(Panier("fruits", "hiver"))
print(Panier("fruits", "été"))
print(Panier("légumes", "hiver"))
print(Panier("légumes", "été"))
print(Panier("fruits", "automne"))