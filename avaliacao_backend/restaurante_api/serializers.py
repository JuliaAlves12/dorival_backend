from rest_framework import serializers
from .models import Clientes, Mesas, Funcionarios, Pedidos, Pagamentos, Categorias, Produtos, ItensPedido, Ingredientes, Produtos_Ingredientes, Fornecedores, Compras

# Criando serializer de Clientes
class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'
        read_only_fields = ['id']


# Criando serializer de Mesas
class MesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesas
        fields = '__all__'
        read_only_fields = ['id']


# Criando serializer de Funcionarios
class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionarios
        fields = '__all__'
        read_only_fields = ['id']


# Criando serializer de Pedidos
class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = '__all__'
        read_only_fields = ['id']


# Criando serializer de Pagamentos
class PagamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamentos
        fields = '__all__'
        read_only_fields = ['id']


# Criando serializer de Categorias
class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'
        read_only_fields = ['id']


# Criando serializer de Produtos
class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'
        read_only_fields = ['id']


# Criando serializer de ItensPedido
class ItensPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensPedido
        fields = '__all__'
        read_only_fields = ['id']


# Criando serializer de Ingredientes
class IngredientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredientes
        fields = '__all__'
        read_only_fields = ['id']


# Criando serializer de Produtos_Ingredientes
class Produtos_IngredientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos_Ingredientes
        fields = '__all__'
        read_only_fields = ['id']


# Criando serializer de Fornecedores
class FornecedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedores
        fields = '__all__'
        read_only_fields = ['id']


# Criando serializer de Compras
class ComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compras
        fields = '__all__'
        read_only_fields = ['id']