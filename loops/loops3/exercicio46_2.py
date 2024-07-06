'''
Lista de entrada: [5, 3, 9, 1, 10]
Função: Encontra e retorna o maior número da lista.
'''


def acha_maior(lista):
    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero

    return maior

lista = [5, 3, 9, 1, 10, 11]
res = acha_maior(lista)
print(res)