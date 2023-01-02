from django.urls import path
from . import views

urlpatterns = [
    path('configuracoes', views.Configuracoes, name='Configs'),
    path('produtos', views.Produtos, name='Produtos'),
    path('', views.Index, name='Home'),
]
