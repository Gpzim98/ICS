def calcula_par_impar(numero):
    if numero % 2 == 0:
        print('Par ' + str(numero))
    else:
        print('Impar')


for numero in range(101):
    calcula_par_impar(numero)