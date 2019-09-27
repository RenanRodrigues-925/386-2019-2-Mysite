from django.contrib import admin

from .models import Despesa

class DespesaAdmin(admin.ModelAdmin):
    list_display = ('data_criacao', 'tipo_dispesa','descricao', 'forma_de_pagamento', 'vencimento', 'quitado')

admin.site.register(Despesa, DespesaAdmin)
