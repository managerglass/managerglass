from django.utils import timezone
from django.db import models
from core.models import Base
from empresaColigada.models import Empresa


UF_SIGLA = [
    ('AL', 'ALAGOAS'),
]

ENQUADRAMENTO_FISCAL = [
    ('LR', 'Lucro Real'),
    ('LP', 'Lucro Presumido'),
    ('SN', 'Simples Nacional'),
    ('SE', 'Simples Nacional, , excesso sublimite de receita bruta')
]

TIPO_PESSOA = [
    ('PF', 'Pessoa Física'),
    ('PJ', 'Pessoa Jurídica'),
]

TIPO_TELEFONE = [
    ('FIX', "Fixo"),
    ('CEL', "Celular"),
    ('FAX', "Fax"),
    ('OUT', "Outro"),
]

TIPO_ENDERECO = [
    ('UNI', 'Único'),
    ('RES', 'Residencial'),
    ('COM', 'Comercial'),
    ('COB', 'Cobrança'),
    ('ENT', 'Entrega'),
    ('OUT', 'Outro'),
]


class Pessoa(Base, models.Model):
    # Dados
    id_Empresa = models.ForeignKey(
        Empresa, related_name="Id_empresa_pessoa", on_delete=models.CASCADE, blank=True)
    tipoPessoa = models.CharField(max_length=2, choices=TIPO_PESSOA)

    informacoes_adicionais = models.CharField(
        max_length=1055, null=True, blank=True)
    # Dados padrao
    endereco_padrao = models.ForeignKey(
        'Endereco', related_name="endereco_padrao", on_delete=models.CASCADE, null=True, blank=True)
    telefone_padrao = models.ForeignKey(
        'Telefone', related_name="telefone_padrao", on_delete=models.CASCADE, null=True, blank=True)
    site_padrao = models.ForeignKey(
        'Site', related_name="site_padrao", on_delete=models.CASCADE, null=True, blank=True)
    email_padrao = models.ForeignKey(
        'Email', related_name="email_padrao", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name= 'Pessoa'
        verbose_name_plural= 'Pessoas'


    def save(self, *args, **kwargs):
        # Atualizar datas criacao edicao
        if not self.data_criacao:
            self.data_criacao = timezone.now()
        self.data_edicao = timezone.now()
        return super(Pessoa, self).save(*args, **kwargs)


class PessoaFisica(Pessoa):
    nome = models.CharField('Nome', max_length=100, null=True, blank=True )
    cpf = models.CharField('Cpf', max_length=32,null=True, blank=True)
    rg = models.CharField('RG', max_length=32, null=True, blank=True)
    nascimento = models.DateField('Nascimenot', null=True, blank=True)

    class Meta:
        verbose_name= 'Pessoa Física'
        verbose_name_plural= 'Pessoas Física'

    def __str__(self):
        return self.nome

    @property
    def format_cpf(self):
        if self.cpf:
            return 'CPF: {}'.format(self.cpf)
        else:
            return ''

    @property
    def format_rg(self):
        if self.rg:
            return 'RG: {}'.format(self.rg)
        else:
            return ''


class PessoaJuridica(Pessoa):
    cnpj = models.CharField('Cnpj', max_length=32, null=True, blank=True)
    razao = models.CharField('Razão', max_length=255, null=True, blank=True)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=255, null=True, blank=True)

    inscricaoEstadual = models.CharField('Incrição Estadual', max_length=32, null=True, blank=True)
    responsavel = models.CharField('Responsável', max_length=32, null=True, blank=True)
    situcao_fiscal = models.CharField(
        max_length=2, null=True, blank=True, choices=ENQUADRAMENTO_FISCAL)
    suframa = models.CharField('Suframa', max_length=16, null=True, blank=True)

    class Meta:
        verbose_name= 'Pessoa Jurídica'
        verbose_name_plural= 'Pessoas Jurídica'

    def __str__(self):
        return self.nome_fantasia

    @property
    def format_cnpj(self):
        if self.cnpj:
            return 'CNPJ: {}'.format(self.cnpj)
        else:
            return ''

    @property
    def format_ie(self):
        if self.inscricaoEstadual:
            return 'IE: {}'.format(self.inscricaoEstadual)
        else:
            return ''

    @property
    def format_responsavel(self):
        if not self.responsavel:
            return ''
        else:
            return 'Representante: {}'.format(self.responsavel)


class Endereco(models.Model):
    pessoa_end = models.ForeignKey(
        Pessoa, related_name="endereco", on_delete=models.CASCADE)
    tipo_endereco = models.CharField(
        max_length=3, null=True, blank=True, choices=TIPO_ENDERECO)
    logradouro = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=16, null=True, blank=True)
    bairro = models.CharField(max_length=64, null=True, blank=True)
    complemento = models.CharField(max_length=64, null=True, blank=True)
    pais = models.CharField(max_length=32, null=True,
                            blank=True, default='Brasil')
    cpais = models.CharField(max_length=5, null=True,
                             blank=True, default='1058')
    municipio = models.CharField(max_length=64, null=True, blank=True)
    cmun = models.CharField(max_length=9, null=True, blank=True)
    cep = models.CharField(max_length=16, null=True, blank=True)
    uf = models.CharField(max_length=3, null=True,
                          blank=True, choices=UF_SIGLA)

    @property
    def format_endereco(self):
        return '{0}, {1} - {2}'.format(self.logradouro, self.numero, self.bairro)

    @property
    def format_endereco_completo(self):
        return '{0} - {1} - {2} - {3} - {4} - {5} - {6}'.format(self.logradouro, self.numero, self.bairro,
                                                                self.municipio, self.cep, self.uf, self.pais)

    def __unicode__(self):
        s = u'%s, %s, %s (%s)' % (
            self.logradouro, self.numero, self.municipio, self.uf)
        return s

    def __str__(self):
        s = u'%s, %s, %s (%s)' % (
            self.logradouro, self.numero, self.municipio, self.uf)
        return s


class Telefone(models.Model):
    pessoaTelefone = models.ForeignKey(
        Pessoa, related_name="telefone", on_delete=models.CASCADE)
    tipo_telefone = models.CharField(
        max_length=8, choices=TIPO_TELEFONE, null=True, blank=True)
    telefone = models.CharField(max_length=32)


class Email(models.Model):
    pessoa_email = models.ForeignKey(
        Pessoa, related_name="email", on_delete=models.CASCADE)
    email = models.CharField(max_length=255)


class Site(models.Model):
    pessoa_site = models.ForeignKey(
        Pessoa, related_name="site", on_delete=models.CASCADE)
    site = models.CharField(max_length=255)
