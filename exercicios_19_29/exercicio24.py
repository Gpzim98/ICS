'''
24 - Crie uma função chamada troca_valores que receba dois valores a e b como parâmetros, troque os valores entre eles e retorne ambos.
Função de Repetição de String:

'''

def troca_valores(a, b):
    tmp = a
    a = b
    b = tmp

    return a, b 


a, b = troca_valores(10, 20)

print(a, b)