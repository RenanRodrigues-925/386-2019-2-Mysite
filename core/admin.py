from django.contrib import admin

# Register your models here.

from .models import Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')

admin.site.register(Contato, ContatoAdmin)
