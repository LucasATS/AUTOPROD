from django.shortcuts import render, redirect
from django.http import HttpResponse
from .formularios import *
import json


def Index(request):
    return render(request, 'index.html')
# def CadGrupo(request):
#     if (request.POST):
#         form = GrupoForm(request.POST)
#         if (form.is_valid()):
#             form.save()

#     form = GrupoForm
#     return render(request, 'CadastroUtil.html', {'GrupoForm': form})


# def CadCidade(request):
#     if (request.POST):
#         form = CidadeForm(request.POST)
#         if (form.is_valid()):
#             form.save()

#     form = CidadeForm
#     return render(request, 'CadastroUtil.html', {'CidadeForm': form})


# def CadUnidade(request):
#     if (request.POST):
#         form = UnidadeForm(request.POST)
#         if (form.is_valid()):
#             form.save()

#     form = UnidadeForm
#     return render(request, 'CadastroUtil.html', {'UnidadeForm': form})

def Configuracoes(request):
    if (UnidadeForm(request.POST)):
        form = UnidadeForm(request.POST)
        if (form.is_valid()):
            form.save()

    if (CidadeForm(request.POST)):
        form = CidadeForm(request.POST)
        if (form.is_valid()):
            form.save()

    if (GrupoForm(request.POST)):
        form = GrupoForm(request.POST)
        if (form.is_valid()):
            form.save()

    context = {
        'UnidadeLista': Unidade.objects.all(),
        'CidadeLista': Cidade.objects.all(),
        'GrupoLista': Grupo.objects.all(),
        'UnidadeForm': UnidadeForm,
        'CidadeForm': CidadeForm,
        'GrupoForm': GrupoForm,
    }

    return render(request, 'pages/configuracoes.html', context=context)


def Produtos(request):
    if (request.POST):
        form = ProdutoForms(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('Produtos')

    context = {
        'form': ProdutoForms,
        'ListaProdutos': Produto.objects.all(),
    }
    return render(request, 'pages/produtos.html', context=context)


def DeletarProduto(request, id):
    if (request.POST):
        Produto.objects.filter(id=id).delete()

    return redirect('Produtos')
