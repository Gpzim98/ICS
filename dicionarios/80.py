'''
80. **Combinação de Dicionários**
    - Crie dois dicionários e combine-os em um único dicionário. Exiba o dicionário resultante.
'''


dicionario1 = {
    "Brasil": "Brasília",
    "Belgica": "Bruxelas",
}


dicionario2 = {
    "Argentina": "Buenos Aires",
    "Alemanha": "Berlim",
    "Egito": "Cairo"
}

dicionario1.update(dicionario2)
print(dicionario1)
