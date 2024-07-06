listas_listas = ["teste", 1, 3, [5, 3, 8, 1, 9], [6, 4, 2, 10, 8], [1, 8, 3, 4, 2], [5, 7, 9, 1, 2]]

for elemento in listas_listas:
    if type(elemento) == list:
        print(min(elemento))
        break
