from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def ex1(request):
    frase = 'ola mundo'

    data = {
        'titulo': 'Exercicio 1. Ola Mundo',
        'descricao_exercicio': 'Faca um programa que mostre a frase Ola mundo ao usuario',
        'frase': frase
    }
    return render(request, 'ex1.html', data)