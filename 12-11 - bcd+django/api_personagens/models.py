from django.db import models

# Create your models here.

class Obra(models.Model):

    TIPO_CHOICES = [
        ('Anime', 'ANIME'),
        ('Filme', 'FILME'),
        ('Serie', 'SERIE'),
        ('Livro', 'LIVRO')
    ]

    titulo =models.CharField(max_lenght=100)
    tipo = models.CharField(max_length=5, choices=TIPO_CHOICES)
    ano_lancamento = models.DateField(null=True, blank=True)
    estudo_produtora = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
    
class AtorDublador(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Personagem(models.Model):

    GENERO_CHOICES = [
        ('F', 'FEMININO'),
        ('M', 'MASCULINO'),
        ('O', 'OUTRO')
    ]

    nome = models.CharField(max_lenght=100)
    idade = models.PositiveIntegerField()   
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    especie = models.CharField(max_length=50)
    descricao = models.TextField()
    ator_dublador = models.ForeignKey(AtorDublador, on_delete=models.SET_NULL, null=True)
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.ator_dublador}'