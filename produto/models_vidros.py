from django.db import models
from .models import Produto
from core.models import Base


class Vidros(Produto):
    espessura = models.IntegerField('Espessura', null=True, blank=False)
    arredondamento = models.IntegerField('Arredondamento', null=True, blank=False)
    metragem_minima = models.DecimalField('Metragem Mínima', max_digits=5, decimal_places=3)

    class Meta:
        verbose_name = 'Vidro'
        verbose_name_plural = 'Vidros'

class BeneficiamentoVidro(Base):
    id_vidro = models.ForeignKey(
        Vidros, related_name="id_beneficiamento_vidro", on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField('Nome do Beneficiamento', max_length=100)


    class Meta:
        verbose_name = 'Beneficiamento'
        verbose_name_plural = 'Beneficiamentos'
