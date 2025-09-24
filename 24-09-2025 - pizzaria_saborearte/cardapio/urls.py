from django.urls import path
from . import views

urlpatterns = [
    path('pizza_do_dia', views.saudacao1, name='Pizza do Dia'),
    path('promocoes', views.saudacao2, name='Promoções'),
]