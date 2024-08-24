from django.shortcuts import render

def homepage(request):
    dados = {
        'titulo_pagina': 'Bem Vindo ao curso do ICS',
        'subtitulo_pagina': 'Curso de Programacao com Python e Django',
        'visitas': 123,
        'lista_visitas': [
            'Gustavo',
            'Kaique',
            'Luiz',
            'Sara L',
            'Sara M',
            'Maria Clara',
            'Ana Ju',
            'Ana',
            'Gregory'
        ],
        'clientes': [
            {'nome': 'fulano', 'data_cadastro': '10/10/2010', 'saldo': 100},
            {'nome': 'ciclano', 'data_cadastro': '10/10/2010', 'saldo': 100},
            {'nome': 'beltrano', 'data_cadastro': '10/10/2010', 'saldo': 100},
            {'nome': 'Maria', 'data_cadastro': '10/10/2010', 'saldo': 100},
            {'nome': 'Jose', 'data_cadastro': '10/10/2010', 'saldo': 100},
            {'nome': 'Joao', 'data_cadastro': '10/10/2010', 'saldo': 100},
            {'nome': 'fulano', 'data_cadastro': '10/10/2010', 'saldo': 100},
            {'nome': 'fulano', 'data_cadastro': '10/10/2010', 'saldo': 100},
        ]
    }

    return render(request, 'index.html', dados)

def clientes(request):
    return render(request, 'clientes.html')

def produtos(request):
    return render(request, 'produtos.html')