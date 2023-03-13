liste = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(len(liste)): # pour chaque élément i de la liste
    liste.append(liste[i]) # ajout de l'élément i à la liste

texte = input("Veuillez saisir votre message: ") # message à chiffrer
clef = int(input("Veuillez saisir votre clef: ")) # clef de chiffrement

# fonction qui chiffre un caractère
def chiffrer(lettre, liste, clef):
    for i in range(len(liste)): # pour chaque élément i de la liste
        if lettre == " ": # si le caractère est un espace
            return " "
        elif liste[i] == lettre: # si le caractère est dans la liste
            return str(liste[i+clef]) # retourne le caractère chiffré

message_chiffre = str() # message chiffré initialisé à une chaîne de caractères vide

for lettre in texte: # pour chaque caractère du message
    message_chiffre += chiffrer(lettre, liste, clef) # ajout du caractère chiffré au message chiffré

print(message_chiffre)