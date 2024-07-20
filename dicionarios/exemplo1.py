dados = {
    "chave": "valor",
    "001":   "Fulano",
    "002":   "Ciclano",
    "003":   "Beltrano"
}


lista = ['Banana', 'Maca', 'Melao', 'Melancia', 'Morango']
tupla = ('Item', 'Segunda')

# Busca sequencial
def acha_elemento(elemento_procurado, lista):
    for item in lista:
        if item == elemento_procurado: return 'Existe'
    
    return 'Nao existe'

print(acha_elemento('Melao', lista))        