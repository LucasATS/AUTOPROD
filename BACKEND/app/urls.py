from django.urls import path
from . import views

urlpatterns = [
    path('configuracoes', views.Configuracoes, name='Configs'),
    path('venda', views.Produtos, name='Venda'),
    path('', views.Index, name='Home'),
    
    path('produtos', views.Produtos, name='Produtos'),
    path('deletar/produto/<int:id>', views.DeletarProduto, name='deletar/produto'),
]