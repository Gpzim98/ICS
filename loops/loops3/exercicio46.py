"Lista de entrada: [5, 3, 9, 1, 10]"
"Função: Encontra e retorna o maior número da lista."


lista_de_entrada = [5, 3, 9, 1, 10, 99]

def maior_numero(lista):
    maior = -999999
    for numero in lista:
        if numero > maior:
            maior = numero

    return maior

resultado = maior_numero(lista_de_entrada)
print(resultado)