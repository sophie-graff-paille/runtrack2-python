# fonction qui calcule deux nombres en fonction d'un opérateur
def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        return "Votre opérateur n'est pas valide"


print(calcule(18, "+", 5))
print(calcule(28, "-", 6))
print(calcule(7, "*", 9))
print(calcule(2, "/", 41))
print(calcule(8, "%", 53))