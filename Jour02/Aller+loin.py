# fonction Triangle qui prend en paramètres les longueurs des 3 côtés d'un triangle
# et qui affiche le type de triangle (équilatéral, rectangle et isocèle, isocèle, rectangle, quelconque)
def Triangle(a, b, c):
    # règle pour un triangle équilatéral
    if a == b == c: 
        print("Le triangle est équilatéral")
    # règle pour un triangle rectangle et isocèle qu'il faut mettre avant la règle pour un triangle isocèle et rectangle pour ne pas avoir de conflit
    elif (a**2 + b**2 == round(c**2) or a**2 + c**2 == round(b**2) or b**2 + c**2 == round(a**2)) and (round(a == b) or round(a == c) or round(b == c)):
        print("Le triangle est rectangle et isocèle")
    # rèle pour un triangle isocèle
    elif a == b or a == c or b == c:
        print("Le triangle est isocèle")
    # règle pour un triangle rectangle
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Le triangle est rectangle")
    # si aucune de ces règles n'est vérifiée, le triangle est quelconque
    else:
        print("Le triangle est quelconque")

Triangle(3, 3, 3)
Triangle(4, 4, 5)
Triangle(3, 4, 5)
Triangle(4, 4, 32**(0.5)) # 5.65685424949 = sqrt(32) = 4*4 + 4*4 (32)
Triangle(3, 2, 4)
Triangle(3, 3, 18**(0.5)) # 4.24264068712 = sqrt(18) = 3*3 + 3*3 (18)

# Djamel m'a fait un cours sur le triangle rectangle et isocèle.
    