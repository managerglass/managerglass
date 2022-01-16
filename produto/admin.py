from django.contrib import admin

# Register your models here.


# Register your models here.

from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id','codigo_auxiliar','codigo_mercado', 'ncm','nome', 'imagem', 'slug', 'data_criacao','data_edicao','usuario_criacao', 'ativo')
