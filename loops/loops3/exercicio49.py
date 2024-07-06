entrada = ["Ola", "mundo", "python", "!"]

def concatenar_elements(lista):
    resultado = ""

    for elemento in lista:
        resultado += elemento

    return resultado

saida = concatenar_elements(entrada)
print(saida)