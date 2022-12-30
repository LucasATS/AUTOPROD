from django.shortcuts import render, redirect
from django.http import HttpResponse
from formularios import *
import json

# PRODUTOS
def CreateProduto(request):
    if(request.POST):
        form = GrupoForm(request.POST)
        if(form.is_valid()):
            form.save()

    form = GrupoForm
    return render(request, 'Templates/CadastroUtil.html', {'form':form})