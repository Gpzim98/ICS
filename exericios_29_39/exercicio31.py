'''
31 - Par ou Ímpar:
Solicite ao usuário que digite um número. 
Determine e mostre se o número é par ou ímpar.
'''
numero = input('Digite um numero: ')

resto = int(numero) % 2

if resto == 0:
    print('Par')
else:
    print('Impar')