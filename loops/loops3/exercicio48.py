'''
Lista de entrada: ["maçã", "banana", "cereja"]
Elemento e: "banana"
Função: Retorna True se e estiver na lista, e False caso contrário.
'''

lista = ["maçã", "banana", "cereja"]
elemento = "bananas"

def varifica_se_elemento_exite(lista, elemento):
    for palavra in lista:
        if palavra == elemento:
            return True
        
    return False

print(varifica_se_elemento_exite(lista, elemento))