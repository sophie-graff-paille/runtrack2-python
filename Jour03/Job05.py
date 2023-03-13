# fonction qui affiche les nombres premiers entre 0 et 1000
def affichenbpremier():
    for n in range(1000):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                print(n)

affichenbpremier()