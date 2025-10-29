from django.db import models

# Create your models here.
class Maquiagem(models.Model):
    nome = models.CharField(max_length=80)
    marca = models.CharField(max_length=80)
    preco = models.DecimalField(decimal_places=2, max_digits=7)

    def __str__(self):
        return f"{self.nome} - {self.marca} - {self.preco}."