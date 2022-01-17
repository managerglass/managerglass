from django.db import models
from .models import Produto
from core.models import Base

class Perfil(Produto):
    comprimento_padrão = models.IntegerField('Comprimento', null=True, blank=False)
    estoque = models.IntegerField('estoque', null=True, blank=False)
    class Meta:
        verbose_name = 'Pefil'
        verbose_name_plural = 'Perfís'

class LinhaAplicacao(models.Model):
    id_perfil = models.ForeignKey(
        Perfil, related_name="id_linha_perfil", on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField('Nome do Perfil', max_length=100)

    class Meta:
        verbose_name = 'Linha Perfil'
        verbose_name_plural = 'Linhas Pefís'


class PefilReclassificao(models.Model):
    id_perfil = models.ForeignKey(
        Perfil, related_name="id_reclassificacao_perfil", on_delete=models.CASCADE, null=True, blank=True)
    quatidade = models.IntegerField('Quantidade', null=True, blank=False)
    comprimento_padrão = models.IntegerField('Comprimento', null=True, blank=False)

    class Meta:
        verbose_name = 'Perfil Reclassificado'
        verbose_name_plural = 'Perfis Reclassificaos'