from django.contrib import admin
from .models import Livro
# Register your models here.

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'nome_autor', 'assunto', 'editora', 'isbn', 'ano_publicacao')

admin.site.register(Livro, LivroAdmin)
