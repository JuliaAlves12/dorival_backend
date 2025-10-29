from rest_framework import serializers
from .models import Maquiagem

class MaquiagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquiagem 
        fields = ['id', 'nome', 'marca', 'preco']
        read_only_fields = ['id']