from django.shortcuts import render
from produtos.models import Produto
from contato.models import Contato, Sugestao


def homepage2(request):
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

def homepage(request):
    return render(request, 'index2.html')

def sobre_loja(request):
    return render(request, 'sobre-loja.html')

def produtos(request):
    todos_produtos = Produto.objects.all()
    dados = {
        "lista_produtos": todos_produtos
    }

    return render(request, 'produtos.html', dados)

def contato(request):
    dados = {}
    if request.method == 'POST':
        _nome = request.POST.get('nome')
        _email = request.POST.get('email')
        _mensage = request.POST.get('mensagem')
        contato = Contato(nome=_nome, email=_email, mensagem=_mensage)
        contato.save()
        dados = {
            'mensagem': 'Seu contato foi enviado com sucesso'
        }

        return render(request, 'contato.html', dados)
    else:
        return render(request, 'contato.html')

def sugestoes(request):
    dados = {}
    if request.method == 'POST':
        _nome = request.POST.get('nome')
        _email = request.POST.get('email')
        _mensage = request.POST.get('mensagem')
        _tipo = request.POST.get('tipo')
        sugestao = Sugestao(nome=_nome, email=_email, mensagem=_mensage, tipo=_tipo)
        sugestao.save()
        dados = {
            'mensagem': 'Sua sugestao foi enviada com sucesso'
        }

        return render(request, 'sugestoes.html', dados)
    else:
        return render(request, 'sugestoes.html')