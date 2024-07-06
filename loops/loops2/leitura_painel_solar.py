dados_painel = [
    ('06:00', 45), # 0
    ('06:30', 47), # 1
    ('07:00', 50), # 2
    ('08:00', 80), # 3
    ('08:30', 65), # 4
    ('09:00', 70)  # 5
]

maximo_horario = ""
maximo_gerado = 0
contador = 0
while contador < len(dados_painel):
    dados = dados_painel[contador]
    if dados[1] >= maximo_gerado:
        maximo_gerado = dados[1]
        maximo_horario = dados[0]

    contador += 1
    

print("----- Relatorio -------")
print("Horario que mais gerou energia: " + maximo_horario)
print("O total gerado nesse horario foi: " + str(maximo_gerado))