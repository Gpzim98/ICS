tupla1 = (1,2,3,'texto', (1,2), [3,4.5])

print(tupla1)
print(tupla1.count([3,4.5]))
print(tupla1.index('texto'))

print('_____________')

for item in tupla1:
    print(item)

print('_____________')

contador = 0
while contador <= len(tupla1) -1:
    print(tupla1[contador])
    contador = contador + 1

print('_____________')

print(tupla1[1:5])