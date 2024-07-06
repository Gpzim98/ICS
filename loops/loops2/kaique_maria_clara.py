dados_painel = [
    ('06:00', 45), # 0
    ('06:30', 47), # 1
    ('07:00', 50), # 2
    ('08:00', 80), # 3
    ('08:30', 65), # 4
    ('09:00', 70)  # 5
]
# Imprimir todos os kw impar

for numero in range(0, len(dados_painel)):
    dados = dados_painel[numero]
    if dados[1] %    2 == 1:
        print(dados[1])