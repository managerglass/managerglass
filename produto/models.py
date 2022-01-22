from django.db import models

# Create your models here.

from django.db import models
from stdimage.models import StdImageField
from core.models import Base

# signals
from django.db.models import signals # sinaliza o objeto para edicao antes ou apos salvar
from django.template.defaultfilters import slugify
from core.models import Base
from empresaColigada.models import Empresa
from clienteFornecedor.models import Fornecedor


class Produto(Base):
    Empresa = models.ForeignKey(
        Empresa, related_name="Id_empresa_produto", on_delete=models.CASCADE,null=True, blank=True)
    codigo_auxiliar = models.CharField('Codigo Auxiliar', max_length=15)
    codigo_mercado = models.CharField('Codigo Padrão do Mercado', max_length=15, null=True)
    codigo_barras = models.CharField('Codigo de Barras',max_length=20, null=True)
    ncm = models.CharField('Codigo Merco-sul', max_length=15, null=True)
    nome = models.CharField('Nome do Produtos', max_length=100)
    imagem = StdImageField('Imagem', upload_to="produto/imagens", variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


    def produto_pre_save(signal, instance, sender, **kwargs):
        instance.slug = slugify(instance.nome)
        signals.pre_save.connect(produto_pre_save, sender=Produto)


class ProdutoPorFornecedor(Produto):
    fornecedor = models.ForeignKey(
        Fornecedor, related_name="id_fornecedor_produto", on_delete=models.CASCADE, null=True, blank=True)
    codigo_fornecedor = models.CharField('Codigo do Fornecedor ', max_length=50 , null=True)
    peso = models.DecimalField('Peso do Produto', max_digits=8, decimal_places=3,null=True, blank=True)
    preco_medio = models.DecimalField('Preço Medio', max_digits=8, decimal_places=3, null=True, blank=True)
    preco_base = models.DecimalField('Último Preço', max_digits=8, decimal_places=3, null=True)
    ultimo_preco_compra = models.DecimalField('Último Preço', max_digits=8, decimal_places=3, null=True)
    data_atualizacao_preco_base = models.DateField('Data atualização do preço base',null=True )

    def __str__(self):
        return self.nome