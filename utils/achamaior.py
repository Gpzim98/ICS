def acha_maior_lista(lista):
    maior_numero = lista[0]

    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero

    return maior_numero