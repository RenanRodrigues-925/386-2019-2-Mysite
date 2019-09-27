from django.contrib import admin

from .models import Compras

class ComprasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricaoProduto', 'unidadeCompra', 'qtdPrevistoMes', 'preco', 'precoMaximo')

admin.site.register(Compras, ComprasAdmin)
