from django.urls import path
from .views import obra_pegar_deletar, personagem_pegar_deletar, ator_pegar_deletar, relacionamento_pegar_deletar, habilidade_pegar_deletar, personagemhabilidade_pegar_deletar, atualizar_obra, atualizar_personagem, atualizar_ator, atualizar_habilidade, atualizar_personagemhabilidade, atualizar_relacionamento

urlpatterns = [
    path('obra/<int:id>/', obra_pegar_deletar, name='obra_pegar_deletar'), 
    path('atualizar_obra/<int:id>/', atualizar_obra, name='atualizar_obra'),
    path('ator/<int:id>/', personagem_pegar_deletar, name='personagem_pegar_deletar'),
    path('atualizar_ator/<int:id>/', atualizar_personagem, name='atualizar_personagem'),
    path('persongem/<int:id>/', ator_pegar_deletar, name='ator_pegar_deletar'),
    path('atualizar_persongem/<int:id>/', atualizar_ator, name='atualizar_ator'),
    path('habilidade/<int:id>/', habilidade_pegar_deletar, name='habilidade_pegar_deletar'),
    path('atualizar_habilidade/<int:id>/', atualizar_habilidade, name='atualizar_habilidade'),
    path('personagemhabilidade/<int:id>/', personagemhabilidade_pegar_deletar, name='personagemhabilidade_pegar_deletar'),
    path('atualizar_personagemhabilidade/<int:id>/', atualizar_personagemhabilidade, name='atualizar_personagemhabilidade'),
    path('relacionamento/<int:id>/', relacionamento_pegar_deletar, name='relacionamento_pegar_deletar'),
    path('atualizar_relacionamento/<int:id>/', atualizar_relacionamento, name='Atualizar_relacionamento')
]

