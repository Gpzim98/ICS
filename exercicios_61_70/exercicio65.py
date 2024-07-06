'''
Exercício 65: Utilizando a lista matriz_numeros 
fornecida no código, escreva um código que 
imprima o maior número na última sublista.
'''
matriz_numeros = [
    [10, 20, 30, 40, 50], 
    [60, 70, 80, 90, 100], 
    [110, 120, 130, 140, 150]
]

def acha_maior_lista(lista):
    maior_numero = lista[0]

    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero

    return maior_numero

res = acha_maior_lista(matriz_numeros[-1])
print(res)