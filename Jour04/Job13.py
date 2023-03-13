L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
new_L = []

for i in L:
    if i not in new_L:
        new_L += [i]
print(new_L)