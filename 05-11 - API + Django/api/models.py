from django.db import models

# Create your models here.

class Loja_julia(models.Model):
    nome_item = models.CharField(max_length=200)
    peso_item = models.FloatField(max_length=50)
    calorias = models.FloatField(max_length=50)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome_item