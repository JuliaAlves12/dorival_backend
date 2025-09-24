from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saudacao(request):
    return HttpResponse("Bem-vindo à Soluções Web Rápidas! Em breve, um novo site para impulsionar o seu negócio.")