from django.urls import path
from .views import obra_pegar_deletar, personagem_pegar_deletar, ator_pegar_deletar, relacionamento_pegar_deletar, habilidade_pegar_deletar, personagemhabilidade_pegar_deletar

urlpatterns = [
    path('obra/<int:id>/', obra_pegar_deletar, name='obra_pegar_deletar'), 
    path('ator/<int:id>/', personagem_pegar_deletar, name='personagem_pegar_deletar'),
    path('persongem/<int:id>/', ator_pegar_deletar, name='ator_pegar_deletar'),
    path('habilidade/<int:id>/', personagemhabilidade_pegar_deletar, name='relacionamento_pegar_deletar'),
    path('personagemhabilidade/<int:id>/', habilidade_pegar_deletar, name='habilidade_pegar_deletar'),
    path('relacionamento/<int:id>/', relacionamento_pegar_deletar, name='personagemhabilidade_pegar_deletar')
]