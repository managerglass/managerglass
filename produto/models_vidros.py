from django.db import models
from .models import ProdutoPorFornecedor
from core.models import Base

class CorVidro(Base):
    nome = models.CharField('Nome da Cor Vidro', max_length=50, null=True)

    class Meta:
        verbose_name = 'Cor do vidro'
        verbose_name_plural = 'Cores dos vidros'

class TipoVidro(Base):
    nome = models.CharField('Nome Tipo Vidro', max_length=50, null=True)

    class Meta:
        verbose_name = 'Tipo vidro'
        verbose_name_plural = 'Tipos vidros'



class Vidros(ProdutoPorFornecedor):
    cor_vidro = models.ForeignKey(
        CorVidro, related_name="id_cor_vidro", on_delete=models.CASCADE, null=True, blank=True)
    tipo_vidro = models.ForeignKey(
        TipoVidro, related_name="id_tipo_vidro", on_delete=models.CASCADE, null=True, blank=True)
    espessura = models.IntegerField('Espessura', null=True, blank=False)
    arredondamento = models.IntegerField('Arredondamento', null=True, blank=False)
    metragem_minima = models.DecimalField('Metragem Mínima', max_digits=5, decimal_places=3)

    class Meta:
        verbose_name = 'Vidro'
        verbose_name_plural = 'Vidros'

class BeneficiamentoVidro(Base):
    vidro = models.ForeignKey(
        Vidros, related_name="id_beneficiamento_vidro", on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField('Nome do Beneficiamento', max_length=100)


    class Meta:
        verbose_name = 'Beneficiamento'
        verbose_name_plural = 'Beneficiamentos'

    def __str__(self):
        return self.nome