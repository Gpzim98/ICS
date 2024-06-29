'''
29 - Calculadora Simples:
Peça ao usuário que digite dois números 
e então pergunte qual operação ele deseja realizar 
(adição, subtração, multiplicação ou divisão). 
Realize a operação e mostre o resultado.

'''

num1 = input('Digite o primeiro numero:')
num2 = input('Digite o segundo numero:')
operacao = input('Digite qual operacao vc deseja: (+ - * /)')

if operacao == '+':
    soma = int(num1) + int(num2)
    print(soma)
elif operacao == '-':
    subtracao = int(num1) - int(num2)
    print(subtracao)  
elif operacao == '*':
    multiplicacao = int(num1) * int(num2)
    print(multiplicacao)
else:
    divisao = int(num1) / int(num2)
    print(divisao)