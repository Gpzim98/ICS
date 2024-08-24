from Classes import Pessoa, Funcionario, Gerente

# pessoa = Pessoa('fulano', 'alves', 30)
# res = pessoa.busca_dados_completos()
# ano_nascimento = pessoa.calcula_ano_nascimento()
# print(ano_nascimento)
# print(res)    

# funcionario = Funcionario('Fulano', 'Da silva', 31)    
# funcionario.add_info_funcionario('Programador', 'Sistemas')
# res = funcionario.busca_dados_completos()
# print(res)

# ano_nascimento = funcionario.calcula_ano_nascimento()
# print(ano_nascimento)

gerente = Gerente('Gerente Fulano', 'Pereira', 40)

gerente.add_info_funcionario('Gerente', 'Marketing')

dados_completos = gerente.busca_dados_completos()

print(dados_completos)

departamento = gerente.busca_departamento()

print(departamento)
