'''
Crie uma classe Produto com uma propriedade preco que não permite 
preços negativos. Crie uma classe derivada ProdutoEletronico 
que adiciona um atributo garantia e um método detalhes() para exibir as informações.
'''

class Produto:
    preco = 0

    def seta_preco(self, _preco):
        if _preco < 0:
            print('preco invalido, o preco nao pode ser negativo')
            return False
        else:
            self.preco = _preco

class ProdutoEletronico(Produto):
    garantia = ''

    def detalhes(self):
        print('Produto de preco:' + str(self.preco))
        print('Garantia: ' + self.garantia)

produto = ProdutoEletronico()
produto.garantia = '12 meses de garantia'
produto.seta_preco(9.99)
print(produto.detalhes())