# fonction qui demande à l'utilisateur de rentrer son nom
# et qui à son appel affiche "Hello" suivi du nom de l'utilisateur
def My_print_name(): 
    name = input("Quel est votre nom ? ")
    return "Hello " + name

print(My_print_name())