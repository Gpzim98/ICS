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

def ex2(request):
    data = {
        'titulo': 'Exercicio 2. Calculo de total',
        'descricao_exercicio': 'Faca um programa que receba 2 numeros do usuario e calcule o total',
    }

    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        total = int(num1) + int(num2)

        data['total'] = total
    
    return render(request, 'ex2.html', data)