lista_cores = ["branco", "preto", "cinza"]

# for indice, cor in enumerate(lista_cores):
#     print(str(indice + 1) + "." + cor)

indice = 0
while indice < len(lista_cores):
    cor = lista_cores[indice]
    print(str(indice + 1) + "." + cor)
    indice+=1
