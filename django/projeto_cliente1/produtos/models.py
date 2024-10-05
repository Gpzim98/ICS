from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    quantidade = models.IntegerField()
    data_cadastro = models.DateField(auto_now=True)
    foto_produto = models.ImageField(upload_to='produtos', blank=True, null=True)
    ativo = models.BooleanField(default=True)
    documento_contrato = models.FileField(upload_to='contratos', blank=True, null=True) 

    def __str__(self):
        return self.nome