from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saudacao1(request):
    return HttpResponse("Hoje, nossa sugestão especial é a Pizza de Calabresa com Catupiry!")

def saudacao2(request):
    return HttpResponse("Aproveite! Na compra de qualquer pizza grande, o refrigerante de 2L é por nossa conta.")