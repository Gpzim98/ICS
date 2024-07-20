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
    endereco = None

    # Metodo construtor 
    def __init__(self, nome_passado, sobrenome_passado, idade_passada, endereco_passado):
        self.nome = nome_passado
        self.sobrenome = sobrenome_passado
        self.idade = idade_passada
        self.endereco = endereco_passado

    def retorna_nome_completo(self):
        return self.nome + self.sobrenome
    
    def imprime_dados_completos(self):
        return 'Dados Completos: ' + self.nome + ' ' + self.sobrenome + ' ' + str(self.idade)

    def modifica_profissao(self, nova_profissao):
        self.profissao = nova_profissao

    def endereco_completo(self):
        return self.endereco
    
    def aniversario(self):
        self.idade +=1

    def modifica_nome(self, novo_nome):
        self.nome = novo_nome