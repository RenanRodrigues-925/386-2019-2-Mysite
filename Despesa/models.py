from django.db import models

class Despesa(models.Model):
    data_criacao = models.DateField()
    tipo_dispesa = models.CharField(max_length=200)
    descricao = models.CharField(max_length=300)
    forma_de_pagamento = models.CharField(max_length=10)
    vencimento = models.DateField()
    quitado = models.BooleanField()

    def __str__(self):
        return self.data_criacao

