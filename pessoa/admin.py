from django.contrib import admin
# Register your models here.


# Register your models here.

from .models import PessoaJuridica
from .models import PessoaFisica



# Register your models here.

@admin.register(PessoaJuridica)
class PessoaJuridicaAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'responsavel', 'nome_fantasia')


@admin.register(PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'rg', 'nascimento')
