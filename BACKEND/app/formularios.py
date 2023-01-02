from django.forms import ModelForm
from .models import *


class GrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = ['grupo']


class CidadeForm(ModelForm):
    class Meta:
        model = Cidade
        fields = ['cidade', 'uf']


class UnidadeForm(ModelForm):
    class Meta:
        model = Unidade
        fields = ['titulo', 'descricao']


# class VendaForms(ModelForm):
#     class Meta:
#         model = Venda
#         fields = ['produtos', 'valorTotal', 'desconto', 'data']


class ProdutoForms(ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'preco', 'margemVenda', 'peso', 'medidas', 'qntEstoque', 'qntMin', 'codExterno', 'grupo', 'unidade']
