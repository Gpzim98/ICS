'''
1,3,5,7,9

4 / 2 = 2 (par)
5 / 2 = 2 (impar)
17 / 2 = 8 (impar)

'''
def par_impar(valor):
    lista_impar = '1,3,5,7,9'
    ultimo_digito = valor[-1]

    if ultimo_digito in lista_impar:
        print("impar")
    else:
        print("par")

while True: 
    valor = input("Digite um numero para descobrir se e par ou impar:")
    par_impar(valor)