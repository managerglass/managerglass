from django.contrib import admin

# Register your models here.


# Register your models here.

from .models_vidros import Vidros
from .models_perfil import Perfil

@admin.register(Vidros)
class VidrosAdmin(admin.ModelAdmin):
    list_display = ('id','codigo_auxiliar','codigo_mercado', 'ncm','nome', 'imagem', 'slug', 'data_criacao','data_edicao','usuario_criacao', 'ativo')



@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id','codigo_auxiliar','codigo_mercado', 'ncm','nome', 'imagem', 'slug', 'data_criacao','data_edicao','usuario_criacao', 'ativo')
