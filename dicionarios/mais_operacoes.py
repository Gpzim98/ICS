dicionario = {
    1: 'Banana', 
    2: 'Maca', 
    3: 'Melao', 
    4: 'Melancia', 
    5: 'Morango',
}

print(dicionario)

# print(dicionario.keys())
# print(dicionario.values())

item_removido = dicionario.pop(2)
print(dicionario)
print(item_removido)

print(dicionario.get(10))

# dicionario.clear()
# print(dicionario)