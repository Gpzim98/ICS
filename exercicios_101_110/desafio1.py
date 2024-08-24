'''
Crie uma class chamada calculadora de impostos 
com o metodo calcular imposto que recebe um valor em dinheiro e retorna 
o percentual de impostos onde a aliquota e fixa em 12%

criar uma classe chamada CalculadoraIof derivada de calculadora_impostos
e adicione um metodo chamado calcular_iof
que retorne 1% do valor passado

crie outra class chamada CalculadoraDeSimplesNacional
derivada de calculadora_impostos que tenha um metodo
para calcular o Simples
no final calcule os 2 impostos e imprima o total
'''

class calculadora_impostos:
    def calcular_impostos(self, valor):
        return (valor * 12) / 100

calculatora = calculadora_impostos()    
print(calculatora.calcular_impostos(100))

class CalculadoraSimples(calculadora_impostos):
    def calcula_simples(self, valor):
        return (valor * 2) / 100
    
calculadora = CalculadoraSimples()
imposto1 = calculadora.calcular_impostos(100)
imposto2 = calculadora.calcula_simples(100)
print(str(imposto1 + imposto2))    
'''
adicione um metodo na CalculadoraSimples chamado calcula_total_imposto
que retorna os impostos totais, (imposto1 + simples)
'''

'''
Crie uma class chamada CalculadoraDespesas
que tenha um metodo chamado calcula_despesas que recebe o faturamento total
e retorna a soma de todos os impostos
esta class pode utilizar as classes existentes

'''