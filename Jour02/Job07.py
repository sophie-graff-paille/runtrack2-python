# fonction qui prend en paramètre un langage de programmation et qui affiche un message en fonction du langage
def Ifiam(langage):
    if langage == "Javascript":
        print("Tu es un développeur web")
    elif langage == "Python":
        print("Tu es un développeur IA")
    elif langage == "java":
        print("Tu es un développeur logiciel")
    elif langage == "reactjs":
        print("Tu es un développeur mobile")
    else:
        print("Un jour, je serai le meilleur développeur...")

Ifiam("Javascript")
Ifiam("Python")
Ifiam("java")
Ifiam("reactjs")
Ifiam("HTML")