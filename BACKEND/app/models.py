from django.db import models
from datetime import date


class Grupo(models.Model):
    def __str__(self):
        return self.grupo

    grupo = models.CharField(max_length=56)


class Unidade(models.Model):
    def __str__(self):
        return self.titulo

    titulo = models.CharField(max_length=16)
    descricao = models.CharField(max_length=126)


class Cidade(models.Model):
    def __str__(self):
        return self.cidade

    cidade = models.CharField(max_length=26)
    uf = models.CharField(max_length=2)


class Produto(models.Model):
    def __str__(self):
        return self.descricao

    descricao = models.CharField(max_length=126)
    preco = models.DecimalField(max_digits=6,  decimal_places=4)
    margemVenda = models.DecimalField(max_digits=5,  decimal_places=3)
    peso = models.DecimalField(max_digits=6,  decimal_places=4)
    medidas = models.CharField(max_length=56)
    qntEstoque = models.IntegerField()
    qntMin = models.IntegerField()
    codExterno = models.CharField(max_length=125, null=True)  # PODE SER O CÓDIGO DE BARRA
    dataCadastro = models.DateField(default=date.today)
    dataModificacao = models.DateField(default=date.today)
    grupo = models.ForeignKey(Grupo, null=True, on_delete=models.CASCADE)
    unidade = models.ForeignKey(Unidade, null=True, on_delete=models.CASCADE)  # cx, cm, m, kg, m2...


class ListaVenda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=5,  decimal_places=3)
    quantidade = models.IntegerField()


class Venda(models.Model):
    produtos = models.ManyToManyField(ListaVenda)
    valorTotal = models.DecimalField(max_digits=5,  decimal_places=3)
    desconto = models.DecimalField(max_digits=5,  decimal_places=3)
    data = models.DateField(default=date.today)


# CLIENTES DO USUARIO
'''
class Endereco(models.Model):
    def __str__(self):
        return self.rua

    rua = models.CharField(max_length=200, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    complemento = models.CharField(max_length=200, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    pais = models.CharField(max_length=50, null=False, blank=False)


class Cliente(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("O", "Outro")
    )

    nome = models.CharField(max_length=256, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=50, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
'''
