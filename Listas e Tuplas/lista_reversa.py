lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)


lista2 = [1, 2, 3, 4, 5]
lista2.clear()
print(lista2)


lista3 = [1, 2, 3, 4, 5]
lista3.extend([7,8,9])
print(lista3)


lista4 = [1, 2, 3, 4, 5]

for elemento in lista4:
    print(elemento)

print('_________________')

contador = len(lista4) -1
while contador >= 0:
    print(lista4[contador])
    contador = contador -1