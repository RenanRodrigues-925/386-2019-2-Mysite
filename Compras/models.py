from django.db import models

class Compras(models.Model):
    nome = models.CharField(max_length=50)
    descricaoProduto = models.CharField(max_length=200)
    unidadeCompra = models.CharField(max_length=50)
    qtdPrevistoMes = models.DecimalField(max_digits=9,decimal_places=2)
    preco = models.DecimalField(max_digits=9,decimal_places=2)
    precoMaximo = models.DecimalField(max_digits=9,decimal_places=2)

    def __str__(self):
        return self.nome
