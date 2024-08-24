'''
Crie uma classe Pessoa com atributos, nome, sobrenome, idade
com um metodo/funcao buscar dados completos, este metodo deve retornar todas as informacoes da pessoa em forma de dicionario

Apos isso, crie uma classe Funcionario que herda de pessoa e adiciona os campos
cargo e departamento

faca com que o metodo na classe Functionario retorne tambem esses 2 novos atributos
'''

class Pessoa:
    # Metodo constructor
    def __init__(self, _nome, _sobrenome, _idade) -> None:
        self.nome = _nome
        self.sobrenome = _sobrenome
        self.idade = _idade

    def calcula_ano_nascimento(self):
        return 2024 - self.idade

    def busca_dados_completos(self):
        return {
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'idade': self.idade
        }

class Funcionario(Pessoa):
    cargo = None
    departamento = None

    def add_info_funcionario(self, cargo, departamento) -> None:
        self.cargo = cargo
        self.departamento = departamento

    def busca_dados_completos(self):
        return {
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'idade': self.idade,
            'cargo': self.cargo,
            'departamento': self.departamento
        }
    
class Gerente(Funcionario):
    def busca_departamento(self):
        return self.departamento    