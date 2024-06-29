'''
Escolha um número secreto entre 1 e 10. 
Peça ao usuário para adivinhar o número. 
Diga a ele se o palpite está correto, ou 
se o número secreto é maior ou menor que o palpite.
'''

numero_secreto = 9
numero_usuario = int(input('Advinhe o numero: '))

if numero_secreto == numero_usuario:
    print('Parabens vc acertou')
elif numero_usuario > numero_usuario:
    print('O numero secreto e maior')    
else:
    print('O numero secreto e menor')