from rest_framework.decorators import api_view
from .models import Obra, AtorDublador, Personagem, Habilidade, PersonagemHabilidades, Relacionamento
from .serializers import ObraSerializer, AtorDubladorSerializer, PersonagemSerializer, HabilidadeSerializer, RelacionamentoSerializer, PersonagemHabilidadesSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'DELETE'])
def obra_pegar_deletar(request,id):
    try:
        obra = Obra.objects.get(pk=id)
    except Obra.DoesNotExist:
        return Response({"Mensagem": "Obra não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ObraSerializer(obra)
        return Response(serializer.data)
    if request.method == "DELETE":
        obra.delete()
        return Response({"Mensagem:" "Obra Deletado com Sucesso"})


@api_view(['GET', 'DELETE'])
def personagem_pegar_deletar(request, id):
    try:
        personagem = Personagem.objects.get(pk=id)
    except Personagem.DoesNotExist:
        return Response({"Mensagem": "Personagem não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = PersonagemSerializer(personagem)
        return Response(serializer.data)
    if request.method == "DELETE":
        personagem.delete()
        return Response({"Mensagem": "Personagem Deletado com Sucesso"})
    

@api_view(['GET', 'DELETE'])
def ator_pegar_deletar(request, id):
    try:
        ator = AtorDublador.objects.get(pk=id)
    except AtorDublador.DoesNotExist:
        return Response({"Mensagem": "Ator não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = AtorDubladorSerializer(ator)
        return Response(serializer.data)
    if request.method == "DELETE":
        ator.delete()
        return Response({"Mensagem": "Ator Deletado com Sucesso"})


@api_view(['GET', 'DELETE'])
def habilidade_pegar_deletar(request, id):
    try:
        habilidade = Habilidade.objects.get(pk=id)
    except Habilidade.DoesNotExist:
        return Response({"Mensagem": "Habilidade não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = HabilidadeSerializer(habilidade_pegar_deletar)
        return Response(serializer.data)
    if request.method == "DELETE":
        habilidade.delete()
        return Response({"Mensagem": "Habilidade Deletada com Sucesso"})


@api_view(['GET', 'DELETE'])
def personagemhabilidade_pegar_deletar(request, id):
    try:
        personagemhabilidades = PersonagemHabilidades.objects.get(pk=id)
    except PersonagemHabilidades.DoesNotExist:
        return Response({"Mensagem": "Personagem com Habilidade não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = PersonagemHabilidadesSerializer(personagemhabilidades)
        return Response(serializer.data)
    if request.method == "DELETE":
        personagemhabilidades.delete()
        return Response({"Mensagem": "Personagem com Habilidade Deletada com Sucesso"})
    

@api_view(['GET', 'DELETE'])
def relacionamento_pegar_deletar(request, id):
    try:
        relacionamento = Relacionamento.objects.get(pk=id)
    except Relacionamento.DoesNotExist:
        return Response({"Mensagem": "Relacionamento não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = RelacionamentoSerializer(relacionamento)
        return Response(serializer.data)
    if request.method == "DELETE":
        relacionamento.delete()
        return Response({"Mensagem": "Relacionamento Deletado com Sucesso"})