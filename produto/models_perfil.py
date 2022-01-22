from django.db import models
from .models import ProdutoPorFornecedor
from core.models import Base

class CorPerfil(Base):
    nome = models.CharField('Nome da Cor Perfil', max_length=50, null=True)

    class Meta:
        verbose_name = 'Cor_do_perfil'
        verbose_name_plural = 'Cores dos perfís'

    def __str__(self):
        return self.nome

class TipoPerfil(Base):
    nome = models.CharField('Nome Tipo Perfil', max_length=50, null=True)

    class Meta:
        verbose_name = 'Tipo Perfil'
        verbose_name_plural = 'Tipos Perfís'

    def __str__(self):
        return self.nome

class LinhaAplicacao(models.Model):
    nome = models.CharField('Nome do Perfil', max_length=100)

    class Meta:
        verbose_name = 'Linha Perfil'
        verbose_name_plural = 'Linhas Pefís'

    def __str__(self):
        return self.nome

class Perfil(ProdutoPorFornecedor):
    cor_perfil = models.ForeignKey(
        CorPerfil, related_name="Cor_Perfil", on_delete=models.CASCADE, null=True, blank=True)
    tipo_perfil = models.ForeignKey(
        TipoPerfil, related_name="Tipo_Perfil", on_delete=models.CASCADE, null=True, blank=True)
    comprimento_padrão = models.IntegerField('Comprimento', null=True, blank=False)
    estoque = models.IntegerField('estoque', null=True, blank=False)
    linha_aplicacao = models.ForeignKey(
        LinhaAplicacao, related_name="id_linha_perfil", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Pefil'
        verbose_name_plural = 'Perfís'


class PefilReclassificao(models.Model):
    perfil = models.ForeignKey(
        Perfil, related_name="id_reclassificacao_perfil", on_delete=models.CASCADE, null=True, blank=True)
    quantidade = models.IntegerField('Quantidade', null=True, blank=False)
    comprimento_padrão = models.IntegerField('Comprimento', null=True, blank=False)

    class Meta:
        verbose_name = 'Perfil Reclassificado'
        verbose_name_plural = 'Perfis Reclassificaos'