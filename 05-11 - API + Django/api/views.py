from django.shortcuts import render
from rest_framework.response import Response
from .models import Loja_julia
from .serializer import Loja_juliaSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def listar_itens(request):
    itens = Loja_julia.objects.all()
    serializer = Loja_juliaSerializer(itens, many=True)
    return Response(serializer.data)