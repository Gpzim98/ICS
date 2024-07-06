'''
Faca um programa que peca ao usuario para digitar
a nota de cada aluno de uma turma de 10
no final o seu programa tem que dizer qual foi a maior nota
'''

def calcula_media():
    contador = 0
    total = 0
    while contador < 4:
        total += int(input('Digite um valor:'))
        contador += 1

    media = total / 4
    return media

resultado = calcula_media()
print(resultado)