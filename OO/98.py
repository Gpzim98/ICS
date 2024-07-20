from Pessoa import Pessoa

pessoa = Pessoa('Fulano', 'de tal', 30, 'Rua x')
print(pessoa.imprime_dados_completos())
pessoa.modifica_nome('Beltrano')
print(pessoa.imprime_dados_completos())