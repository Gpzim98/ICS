from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=80)
    endereco = models.CharField(max_length=150)
    data_nascimento = models.CharField(max_length=10)
    escolaridade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome + " " + self.sobrenome
    