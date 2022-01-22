from django.contrib import admin

# Register your models here.


# Register your models here.

from .models_vidros import Vidros
from .models_perfil import Perfil, LinhaAplicacao, PefilReclassificao, CorPerfil, TipoPerfil
from .models_componentes import  ComponentesAcessorios, CorComponentes, GrupoAplicacao, Tipo

@admin.register(Vidros)
class VidrosAdmin(admin.ModelAdmin):
    list_display = ('id','codigo_auxiliar','codigo_mercado', 'ncm','nome', 'imagem', 'slug', 'data_criacao','data_edicao','usuario_criacao', 'ativo')

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id','codigo_auxiliar','codigo_mercado', 'ncm','nome', 'imagem', 'slug', 'data_criacao','data_edicao','usuario_criacao', 'ativo')

@admin.register(LinhaAplicacao)
class LinhaAplicacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

@admin.register(TipoPerfil)
class TipoPerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

@admin.register(CorPerfil)
class CorPerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

@admin.register(PefilReclassificao)
class PerfilReclassificacao(admin.ModelAdmin):
    list_display = ('id', 'quantidade')

@admin.register(GrupoAplicacao)
class ComponentesAplicacao(admin.ModelAdmin):
    list_display = ('id', 'nome')

@admin.register(Tipo)
class ComponentesTipo(admin.ModelAdmin):
    list_display = ('id', 'nome')

@admin.register(CorComponentes)
class ComponentesCor(admin.ModelAdmin):
    list_display = ('id', 'nome')
