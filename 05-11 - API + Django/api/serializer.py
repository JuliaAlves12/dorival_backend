from rest_framework import serializers
from .models import Loja_julia

class Loja_juliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja_julia
        fields = ['id', 'nome_item', 'peso_item', 'calorias', 'preco']
        read_only_fields = ['id']