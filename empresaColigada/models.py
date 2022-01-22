
# Create your models here.
from django.utils import timezone

from django.db import models
from core.models import Base


class Empresa(Base, models.Model):
    cnpj = models.CharField('Cnpj', max_length=32, null=True, blank=True)
    nome_fantasia = models.CharField('Nome Fantasia',max_length=255, null=True, blank=True)
    matriz_coligada = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    responsavel = models.CharField('Responsável',max_length=32, null=True, blank=True)
    email = models.CharField('E-mail', max_length=120, null=True, blank=True)

    class Meta:
        verbose_name= 'Empresa'
        verbose_name_plural= 'Empresas'

    def __str__(self):
        return self.nome_fantasia



