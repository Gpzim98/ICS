lista_numeros = [1,2,3,4]
lista_palavras = ['Pirapora', 'Buritizeiro', "Varzea da Palma"]
lista_float = [1.2, 4.5, 7.8]

lista_listas = [
    [1,2,3,5], 
    ['Palavra1', 'Palavra2'], 
    [4.5, 6.7, 8.9]
]

# append -> adicionar na lista
minha_lista = []
minha_lista.append(1)
minha_lista.append(['Pirapora'])
minha_lista.append(['Pirapora'])
res = minha_lista.pop(0) # Remove o ultimo item da lista
minha_lista.remove(['Pirapora'])
print(res)
print(minha_lista)