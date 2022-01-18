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
    id_Empresa = models.ForeignKey(
        Empresa, related_name="Id_empresa_produto", on_delete=models.CASCADE,null=True, blank=True)
    codigo_auxiliar = models.CharField('codigo Auxiliar', max_length=15)
    codigo_mercado = models.CharField('codigo Padrão do Mercado', max_length=15, null=True)
    ncm = models.CharField('codigo Merco-sul', max_length=15, null=True)
    nome = models.CharField('Nome do Produtos', max_length=100)
    imagem = StdImageField('Imagem', upload_to="produto/imagens", variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


    def produto_pre_save(signal, instance, sender, **kwargs):
        instance.slug = slugify(instance.nome)
        signals.pre_save.connect(produto_pre_save, sender=Produto)


class ProdutoPorFornecedor(Produto):
    id_fornecedor = models.ForeignKey(
        Fornecedor, related_name="id_fornecedor_produto", on_delete=models.CASCADE, null=True, blank=True)
