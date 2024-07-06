a = 2
b = 20
c = 19

if a > b:
    print("A e maior")
    print("A e bem maior que b")
elif b > c:
    print("B e maior que C")    
else:
    print("C e o maior")


a = 8
b = 7
c = 9

if a < b:
    print("A e menor que b")
elif b < c:
    print("B e menor que c")
else:
    print("C e o menor")


if a < b and b < c:
    print(">>> C e o maior numero")    
elif a > b and b < c:
    print(">>> B e o menor")

a = 31
b = 31
c = 30

if a < b or b < c:
    print(":::: Executou esse if")

if a == b:
    print("-------Eles sao iguais")    

a = 12
b = 11
if a <= b:
    print("-:-:- Os numeros sao igais ou a e menor que b")    
elif a >= b:
    print("-:-:- A e maior ou igual a b")