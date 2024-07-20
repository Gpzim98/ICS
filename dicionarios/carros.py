carro = {
    'Marca': 'Chevrolet',
    'Ano': 1989,
    'KmRodados': 5677856,
    'NPortas': 2,
    'LitrosTanque': 50,
    'UltimosDonos': {
        '1': ['Fulano',  1989],
        '2': ['Ciclano', 1999],
        '3': ['Beltrano', 2000]
    }
}

print('Tamanho do tanque:' + str(carro.get('LitrosTanque')))

ultimosDonos = carro.get('UltimosDonos')
ultimoDono = ultimosDonos.get('1')
print(ultimoDono[0])
