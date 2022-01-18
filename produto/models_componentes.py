from django.db import models
from .models import ProdutoPorFornecedor
from core.models import Base


class CorComponentes(Base):
    nome = models.CharField('Nome da Cor', max_length=50, null=True)

    class Meta:
        verbose_name = 'Cor do Componente'
        verbose_name_plural = 'Cores dos Componentes'


class GrupoAplicacao(Base):
    nome = models.CharField('Nome da Aplicação', max_length=50, null=True)

    class Meta:
        verbose_name = 'Grupo Aplicação Componentes'
        verbose_name_plural = 'Grupos Aplicações Componentes'


class Tipo(Base):
    nome = models.CharField('Nome Tipo', max_length=50, null=True)

    class Meta:
        verbose_name = 'Tipo Componente'
        verbose_name_plural = 'Tipos Componentes'


class ComponentesAcessorios(ProdutoPorFornecedor):
    id_cor_componentes = models.ForeignKey(
        CorComponentes, related_name="id_cor_componentes", on_delete=models.CASCADE, null=True, blank=True)
    id_tipo_componentes = models.ForeignKey(
        Tipo, related_name="id_tipo_componentes", on_delete=models.CASCADE, null=True, blank=True)
    id_grupo_aplicacao = models.ForeignKey(
        GrupoAplicacao, related_name="id_grupo_componentes", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Vidro'
        verbose_name_plural = 'Vidros'