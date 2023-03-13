def length(L):
    total = 0
    for i in L:
        total += 1
    return total

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
print(length(L))

def croissant(L):
    i = 0
    for i in range(length(L)):
        for j in range(i+1, length(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    return L
print(croissant(L))