'''
30 - Comparador de Números:
Peça ao usuário para inserir dois números. 
Informe qual número é maior ou se eles são iguais.
'''
num1 = input('Digite o primeiro numero:')
num2 = input('Digite o segundo numero:')

if int(num1) > int(num2):
    print('O primeiro numero e o maior: ' + num1)
elif int(num2) > int(num1):
    print('O segundo numero e o maior: ' + num2)
else:
    print('Eles sao iguais')