from django.db import models
from pessoa.models import  PessoaJuridica
from core.models import Base
# Create your models here.

class FornecedorTipo(Base):
    nome = models.CharField('Nome Tipo Fornecedor', max_length=50, null=True)

    class Meta:
        verbose_name = 'Tipo Fornecedor'
        verbose_name_plural = 'Tipo Fornecedores'

class Fornecedor(PessoaJuridica):
    id_tipo_fornecedor = models.ForeignKey(
        FornecedorTipo, related_name="id_tipo_fornecedor", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'