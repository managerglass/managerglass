# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    data_criacao = models.DateTimeField('Data de Criação', auto_now=True)
    data_edicao = models.DateTimeField('Data de Edição', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)
    usuario_criacao = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True


