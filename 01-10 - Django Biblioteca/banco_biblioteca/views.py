from django.shortcuts import render
from django.http import HttpResponse

def saudacao(request):
    return HttpResponse("Olá, bem-vindo(a) à Biblioteca da Júlia Alves!")
