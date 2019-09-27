from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    nome_autor = models.CharField(max_length=50)
    assunto = models.CharField(max_length=100)
    editora = models.CharField(max_length=30)
    isbn = models.CharField(max_length=20)
    ano_publicacao = models.DateField()

    def __str__(self):
        return self.titulo
