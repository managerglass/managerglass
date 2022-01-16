
# Create your models here.
from django.utils import timezone

from django.db import models
from core.models import Base


class Empresa(Base, models.Model):
    cnpj = models.CharField(max_length=32, null=True, blank=True)
    nome_fantasia = models.CharField(max_length=255, null=True, blank=True)
    matriz = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    responsavel = models.CharField(max_length=32, null=True, blank=True)
    email = models.CharField(max_length=120, null=True, blank=True)



