from django.db import models

class Apartamento(models.Model):
    numero = models.IntegerField()
    qtdQuartos = models.IntegerField()
    proprietario = models.CharField(max_length=50)
    valorCondominio = models.DecimalField(max_digits=9,decimal_places=2)

    def __str__(self):
        return self.numero
