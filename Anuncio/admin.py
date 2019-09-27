from django.contrib import admin

from .models import Anuncio

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'textoTitulo', 'preco', 'textoAnuncio', 'nomeContato', 'telefone', 'secao', 'tipoAnuncio')

admin.site.register(Anuncio, AnuncioAdmin)