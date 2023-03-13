liste = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(len(liste)):
    liste.append(liste[i])

texte = input("Veuillez saisir votre message: ")
clef = int(input("Veuillez saisir votre clef: "))

def chiffrer(lettre, liste, clef):
    for i in range(len(liste)):
        if lettre == " ":
            return " "
        elif liste[i] == lettre:
            return str(liste[i+clef])

message_chiffre = str()

for lettre in texte:
    message_chiffre += chiffrer(lettre, liste, clef)

print(message_chiffre)