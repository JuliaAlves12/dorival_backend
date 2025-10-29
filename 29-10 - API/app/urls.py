from .views import listar_maquiagem
from django.urls import path

urlpatterns = [
    path('maquiagens/', listar_maquiagem)
]