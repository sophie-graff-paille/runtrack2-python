# fonction qui affiche les nombres de 1 à 100
#qui remplace les multiples de 3 par Fizz, les multiples de 5 par Buzz et les multiples de 3 et 5 par FizzBuzz
def affichenb4():
    i = 0
    while (i <= 100): # tant que i est inférieur ou égal à 100
        i += 1 # on incrémente i de 1
        if (i % 3 == 0 and i % 5 == 0): # si i est divisible par 3 et 5
            print("FizzBuzz")
        elif (i % 3 == 0): # si i est divisible par 3
            print("Fizz")
        elif (i % 5 == 0): # si i est divisible par 5
            print("Buzz")
        else: 
            print(i) # sinon affiche uniquement le nombre

affichenb4()