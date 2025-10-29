from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Maquiagem
from .serializers import MaquiagemSerializer
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def listar_maquiagem(request):
    maquiagens = Maquiagem.objects.all()
    serializer = MaquiagemSerializer(maquiagens, many = True)
    return Response(serializer.data)