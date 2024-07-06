# 14 - Escreva um programa que tenha duas variáveis a e b com valores numéricos, troque os valores entre elas e, em seguida, imprima os novos valores de a e b.


a = 10
b = 20

tmp = a

a = b
b = tmp

print(a, b)

c = 15
d = 25

c, d = d, c

print(c, d)