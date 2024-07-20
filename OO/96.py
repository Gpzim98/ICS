from Estudante import Estudante

estudante = Estudante(
    'Estudante', 
    'De Programacao',
    20,
    'Rua Abcd numero 1')

estudante.altera_curso('Analise e desenvolvimento de sistemas')

print(estudante.retorna_nome_completo())
print(estudante.retorna_curso())