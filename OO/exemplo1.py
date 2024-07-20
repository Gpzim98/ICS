# classes
# objetos

'''
Estilo procedural - o que vinhamos usando ate o momento
x
OO - Estilo de programacao
Que se baseia em modelar um problem atras de classes (modelar)
    As classes possuem dados e comportamentos
    Dados = Representa as informacoes do problema no mundo real
    Comportamento = O que vc faz com aqueles dados. Como vc manipula os dados
'''

class Pessoa:
    nome = ''
    sobrenome = ''
    idade = None
    profissao = 'Engenheiro'

    # Metodo construtor 
    def __init__(self, nome_passado, sobrenome_passado, idade_passada):
        self.nome = nome_passado
        self.sobrenome = sobrenome_passado
        self.idade = idade_passada

    def retorna_nome_completo(self):
        return self.nome + self.sobrenome
    
    def imprime_dados_completos(self):
        return self.nome + ' ' + self.sobrenome + ' ' + str(self.idade)

# Instanciar um objeto
pessoa = Pessoa('Fulano', 'De tal', 33)
print(pessoa.imprime_dados_completos())

pessoa2 = Pessoa('Beltrano', 'Silva', 43)
print(pessoa2.imprime_dados_completos())