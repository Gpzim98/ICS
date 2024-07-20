'''
Modelagem de um dominio/problema
Voce precisa desenvolver a parte de pedidos de um sistema online
O pedido deve conter, id, os itens do pedido, a qtd de cada item
a data e hora do pedido
o preco de cada item
o valor de impostos do pedido
o valor de desconto do pedido
o valor total do pedido
'''
from typing import List

aliquota_imposto = 14

# A classe e a planta de uma casa
class ItemPedido:
    codigoBarra = None
    preco = None
    qtd = 0

    def __init__(self, codigoBarra, preco, qtd):
        self.codigoBarra = codigoBarra
        self.preco = preco
        self.qtd = qtd

# self da acesso as variaveis da classe
class Pedido:
    id: int = None
    itensPedido = List[ItemPedido] 
    impostos = 0
    desconto = 0
    sub_total = 0
    total = 0

    def __init__(self, itensPedido: List[ItemPedido], desconto: float):
        self.id = 1
        self.itensPedido = itensPedido
        self.desconto = desconto

    def calcula_subtotal(self):
        subtotal = 0
        for item in self.itensPedido:
            subtotal += item.preco * item.qtd

        self.sub_total = subtotal

    def calcula_imposto(self):
        self.impostos = (self.sub_total * aliquota_imposto) / 100;    

    def calcula_desconto(self):
        self.desconto = (self.sub_total * self.desconto) / 100

    def calcula_total(self):
        self.total = self.sub_total + self.impostos - self.desconto

# Instanciando/criando um objecto do tipo ItemPedido
item1 = ItemPedido('1234', 10, 2)    
item2 = ItemPedido('1235', 7, 3)    

novo_pedido = Pedido(itensPedido=[item1, item2], desconto=50)
novo_pedido.calcula_subtotal()
novo_pedido.calcula_imposto()
novo_pedido.calcula_desconto()
novo_pedido.calcula_total()

print(novo_pedido)