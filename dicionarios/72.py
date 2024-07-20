'''
72. **Acessando Valores em um Dicionário**
   - Usando o dicionário criado no exercício anterior, escreva um programa que pergunte 
   ao usuário o nome de um país e exiba a capital correspondente.

'''

Paises_capitais = {
    "Brasil": "Brasília",
    "França": "Paris",
    "Japão": "Tóquio",
    "Canadá": "Ottawa",
    "Austrália": "Camberra"
}

pais_usuario = input('Digite um pais para saber a capital: ')

print(Paises_capitais[pais_usuario])