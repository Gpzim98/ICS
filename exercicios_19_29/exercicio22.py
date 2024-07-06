'''
22 - Faça uma função chamada concatena que receba duas strings, 
parte1 e parte2, como parâmetros, una-as em uma nova string e 
retorne essa nova string.
'''
def concatena(parte1, parte2):
    nova_string = parte1 + parte2
    return nova_string

res = concatena("Ola, ", " eu sou o Enzo")
print(res)