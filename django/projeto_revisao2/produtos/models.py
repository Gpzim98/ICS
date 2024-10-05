from django.db import models

class Produto(models.Model):
    CATEGORY_CHOICES = [
        ('ELEC', 'Electronics'),
        ('FASH', 'Fashion'),
        ('FOOD', 'Food'),
        ('BOOK', 'Books'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='ELEC')
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    quantidade = models.IntegerField()
    data_cadastro = models.DateField()
    foto_produto = models.ImageField(upload_to='produtos', blank=True, null=True)

    def __str__(self):
        return "Produto: " + self.nome
  