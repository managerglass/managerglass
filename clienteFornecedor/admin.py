from django.contrib import admin
from .models import Fornecedor, FornecedorTipo
# Register your models here.

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_fantasia')

@admin.register(FornecedorTipo)
class FornecedorTipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
