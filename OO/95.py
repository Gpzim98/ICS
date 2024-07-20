from Pessoa import Pessoa

pessoa1 = Pessoa('Fulano', 'De tal', 33, 'Endereco x')
pessoa2 = Pessoa('Beltrano', 'De tal', 34, 'Endereco y')
pessoa3 = Pessoa('Ciclano', 'De tal', 35, 'Endereco xr')
pessoa4 = Pessoa('Fulano 2', 'De tal', 36, 'Endereco z')


lista_pessoas = [pessoa1, pessoa2, pessoa3, pessoa4]

for pessoa in lista_pessoas:
    print(pessoa.imprime_dados_completos())