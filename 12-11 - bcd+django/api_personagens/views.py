from rest_framework.decorators import api_view
from .models import Obra, AtorDublador, Personagem
from .serializers import ObraSerializer, AtorDubladorSerializer, PersonagemSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def obra_detalhe(request,id):
    obra = Obra.objects.get(pk=id)
    serializer = ObraSerializer(obra)
    return Response(serializer.data)