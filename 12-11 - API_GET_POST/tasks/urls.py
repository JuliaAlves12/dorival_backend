from django.urls import path
from .views import listar_criar_task

urlpatterns = [
    path('tasks/', listar_criar_task,)
]