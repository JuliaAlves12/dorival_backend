from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    isbn = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return f"{self.titulo} - {self.isbn} - {self.descricao}"
    
class Autor(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    biografia = models.TextField()

    def __str__(self):
        return f"{self.nome} - {self.data_nascimento} - {self.biografia}"
    
class Liv_Aut(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE),
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)


class Categoria(models.Model):
    categoria = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.categoria}"
    
class Liv_Categ(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE),
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Nivel_Associacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome}"
    
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    num_identificacao = models.IntegerField()
    email = models.CharField()
    data_cadastro = models.DateField()
    id_associacao = models.ForeignKey(Nivel_Associacao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.num_identificacao} - {self.email} - {self.data_cadastro} - {self.id_associacao}"
    
class Emprestimo(models.Model):
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()
    data_devolucao_limite = models.DateField()
    id_livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)