'''
Data a lista [1,2,3,4,5]
retorne outra lista com [1,4,9,16,25]
'''
lista = [1,2,3,4,5]

def multiplica(lista):
    nova_lista = []
    for numero in lista:
        resultado = numero * numero
        nova_lista.append(resultado)
    return nova_lista

print(multiplica(lista))