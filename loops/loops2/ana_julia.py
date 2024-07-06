dados_painel = [
    ('06:00', 45), # 0
    ('06:30', 47), # 1
    ('07:00', 50), # 2
    ('08:00', 80), # 3
    ('08:30', 65), # 4
    ('09:00', 70)  # 5
]
# Imprimir o dobro dos kw qdo for 08:00
contador = 0

while contador < len(dados_painel):
    dados = dados_painel[contador]
    if dados[0] == '08:00':
        print(dados[1] * 2)
    contador += 1