from django.db import models

class Anuncio(models.Model):
    cliente = models.CharField(max_length=50)
    textoTitulo = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=9,decimal_places=2)
    textoAnuncio = models.CharField(max_length=150)
    nomeContato = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    secao = models.CharField(max_length=50)
    tipoAnuncio = models.CharField(max_length=150)

    def __str__(self):
        return self.cliente