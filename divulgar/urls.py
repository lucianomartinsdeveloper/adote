from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('novo_pet/', views.novo_pet, name='novo_pet'),
    path('atualizar_pet/<int:pk>/', views.atualizar_pet, name='atualizar_pet'),
    path('remover_pet/<int:id>/', views.remover_pet, name="remover_pet"),
    path('ver_pet/<int:id>/', views.ver_pet, name="ver_pet"),
    path('ver_pedido_adocao/', views.ver_pedido_adocao, name="ver_pedido_adocao"),
]