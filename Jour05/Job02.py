# fonction qui dessine un rectangle avec en paramètres la largeur et la hauteur
def draw_rectangle(width, height):
    for i in range(height): # pour chaque élément i de la liste L
        if i == 0 or i == height - 1: # si i est égal à 0 ou à la longueur de la liste L moins 1
            print("|" + "-" * (width - 2) + "|") # affichage de la ligne du haut et du bas
        else:
            print("|" + " " * (width - 2) + "|") # affichage de la ligne du milieu

    print()
draw_rectangle(10, 3)