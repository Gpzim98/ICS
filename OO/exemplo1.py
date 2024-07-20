from Pessoa import Pessoa

def comparar_idade(pessoa1, pessoa2):
    if pessoa1.idade > pessoa2.idade:
        print("Pessoa 1 e a mais velha")
    elif pessoa2.idade > pessoa1.idade:
        print('Pessoa 2 e a mais velha')
    else:
        print('Elas tem a mesma idade')

# Instanciar um objeto
pessoa = Pessoa('Fulano', 'De tal', 33, '')
print(pessoa.imprime_dados_completos())

pessoa2 = Pessoa('Beltrano', 'Silva', 43, 'Avenida Manoel Joaquim de Melo 806')
print(pessoa2.imprime_dados_completos())

pessoa2.modifica_profissao('Enfermeiro')
print(pessoa2.profissao)
print(pessoa2.endereco_completo())
pessoa2.aniversario()
print(pessoa2.idade)
comparar_idade(pessoa, pessoa2)

