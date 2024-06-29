'''
Escolha um número secreto entre 1 e 10. 
Peça ao usuário para adivinhar o número. 
Diga a ele se o palpite está correto, ou 
se o número secreto é maior ou menor que o palpite.
'''

import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 0

    print('bem-vindo ao jogo de adivinhacao')

    while True:
        palpite = int(input('digite um numero entre 1 e 10: '))

        if palpite == numero_secreto:
            print(f'parabens voce acertou o numero secreto {numero_secreto} em {tentativas} tentativas')
            break
        elif palpite < numero_secreto:
            print('errou, numero secreto maior ,tente novamente.')
        else:
            print('errou, numero secreto e menor, tente novamente.')
        
        tentativas += 1

jogo_adivinhacao()