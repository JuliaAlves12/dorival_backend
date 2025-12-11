from django.shortcuts import render
from rest_framework.response import Response
from .models import Clientes, Mesas, Funcionarios, Pedidos, Pagamentos, Categorias, Produtos, ItensPedido, Ingredientes, Produtos_Ingredientes, Fornecedores, Compras
from .serializers import ClientesSerializer, MesasSerializer, FuncionariosSerializer, PedidosSerializer, PagamentosSerializer, CategoriasSerializer, ProdutosSerializer, ItensPedidoSerializer, IngredientesSerializer, Produtos_IngredientesSerializer, FornecedoresSerializer, ComprasSerializer
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

#Criando as views de Clientes
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def listar_atualizar_deletar_cliente(request, id):
    try:
        cliente = Clientes.objects.get(pk=id)
    except Clientes.DoesNotExist:
        return Response({"Mensagem": "Cliente não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ClientesSerializer(cliente)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ClientesSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Cliente atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = ClientesSerializer(cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Cliente atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        cliente.delete()
        return Response({"Mensagem": "Cliente deletado com sucesso"})
    
@api_view(['GET', 'POST'])
def criar_pegar_cliente(request):
    if request.method == 'GET':
        cliente = Clientes.objects.all()
        serializer = ClientesSerializer(cliente, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ClientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "DEU CERTO!!"}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    
#Criando as views de Mesas
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def listar_atualizar_deletar_mesa(request, id):
    try:
        mesa = Mesas.objects.get(pk=id)
    except Mesas.DoesNotExist:
        return Response({"Mensagem": "Mesa não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MesasSerializer(mesa)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = MesasSerializer(mesa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Mesa atualizada com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = MesasSerializer(mesa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Mesa atualizada com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        mesa.delete()
        return Response({"Mensagem": "Mesa deletada com sucesso"})
    
@api_view(['GET', 'POST'])
def criar_pegar_mesa(request):
    if request.method == 'GET':
        mesa = Mesas.objects.all()
        serializer = MesasSerializer(mesa, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = MesasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "DEU CERTO!!"}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    
#Criando as views de Funcionários
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def listar_atualizar_deletar_funcionarios(request, id):
    try:
        funcionario = Funcionarios.objects.get(pk=id)
    except Funcionarios.DoesNotExist:
        return Response({"Mensagem": "Funcionário não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FuncionariosSerializer(funcionario)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = FuncionariosSerializer(funcionario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Funcionário atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = FuncionariosSerializer(funcionario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Funcionário atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        funcionario.delete()
        return Response({"Mensagem": "Funcionário deletado com sucesso"})
    
@api_view(['GET', 'POST'])
def criar_pegar_funcionario(request):
    if request.method == 'GET':
        funcionario = Funcionarios.objects.all()
        serializer = FuncionariosSerializer(funcionario, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = FuncionariosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "DEU CERTO!!"}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

#Criando as views de Pedidos
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def listar_atualizar_deletar_pedido(request, id):
    try:
        pedido = Pedidos.objects.get(pk=id)
    except Pedidos.DoesNotExist:
        return Response({"Mensagem": "Pedido não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer =PedidosSerializer(pedido)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PedidosSerializer(pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Pedido atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = PedidosSerializer(pedido, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Pedido atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        pedido.delete()
        return Response({"Mensagem": "Pedido deletado com sucesso"})
    
@api_view(['GET', 'POST'])
def criar_pegar_pedido(request):
    if request.method == 'GET':
        pedido = Pedidos.objects.all()
        serializer = PedidosSerializer(pedido, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PedidosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "DEU CERTO!!"}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
#Criando as views de Pagamento
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def listar_atualizar_deletar_pagamento(request, id):
    try:
        pagamento = Pagamentos.objects.get(pk=id)
    except Pagamentos.DoesNotExist:
        return Response({"Mensagem": "Pagamento não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer =PagamentosSerializer(pagamento)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PagamentosSerializer(pagamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Pagamento atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = PagamentosSerializer(pagamento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Pagamento atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        pagamento.delete()
        return Response({"Mensagem": "Pagamento deletado com sucesso"})
    
@api_view(['GET', 'POST'])
def criar_pegar_pagamento(request):
    if request.method == 'GET':
        pagamento = Pagamentos.objects.all()
        serializer = PagamentosSerializer(pagamento, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PagamentosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "DEU CERTO!!"}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
#Criando as views de Categorias
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def listar_atualizar_deletar_categoria(request, id):
    try:
        categoria = Categorias.objects.get(pk=id)
    except Categorias.DoesNotExist:
        return Response({"Mensagem": "Categorias não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CategoriasSerializer(categoria)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CategoriasSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Categoria atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = CategoriasSerializer(categoria, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Categoria atualizada com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        categoria.delete()
        return Response({"Mensagem": "Categoria deletada com sucesso"})
    
@api_view(['GET', 'POST'])
def criar_pegar_categoria(request):
    if request.method == 'GET':
        categoria = Categorias.objects.all()
        serializer = CategoriasSerializer(categoria, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CategoriasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "DEU CERTO!!"}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
#Criando as views de Produtos
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def listar_atualizar_deletar_produto(request, id):
    try:
        produto = Produtos.objects.get(pk=id)
    except Produtos.DoesNotExist:
        return Response({"Mensagem": "Produto não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProdutosSerializer(produto)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProdutosSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Produto atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = ProdutosSerializer(produto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Produto atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        produto.delete()
        return Response({"Mensagem": "Produto deletado com sucesso"})
    
@api_view(['GET', 'POST'])
def criar_pegar_produto(request):
    if request.method == 'GET':
        produto = Produtos.objects.all()
        serializer = ProdutosSerializer(produto, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProdutosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "DEU CERTO!!"}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


#Criando as views de ItensPedido
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def listar_atualizar_deletar_itenspedido(request, id):
    try:
        itenspedido = ItensPedido.objects.get(pk=id)
    except ItensPedido.DoesNotExist:
        return Response({"Mensagem": "Item do Pedido não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ItensPedidoSerializer(itenspedido)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ItensPedidoSerializer(itenspedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Item do Pedido atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = ItensPedidoSerializer(itenspedido, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Item do Pedido atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        itenspedido.delete()
        return Response({"Mensagem": "Item do Pedido deletado com sucesso"})
    
@api_view(['GET', 'POST'])
def criar_pegar_itenspedido(request):
    if request.method == 'GET':
        itenspedido = ItensPedido.objects.all()
        serializer = ItensPedidoSerializer(itenspedido, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ItensPedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "DEU CERTO!!"}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

#Criando as views de Ingredientes
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def listar_atualizar_deletar_ingrediente(request, id):
    try:
        ingredientes = Ingredientes.objects.get(pk=id)
    except Ingredientes.DoesNotExist:
        return Response({"Mensagem": "Ingrediente não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = IngredientesSerializer(ingredientes)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = IngredientesSerializer(ingredientes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Ingrediente atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = IngredientesSerializer(ingredientes, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Ingredientes atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        ingredientes.delete()
        return Response({"Mensagem": "Ingredientes deletado com sucesso"})
    
@api_view(['GET', 'POST'])
def criar_pegar_ingrediente(request):
    if request.method == 'GET':
        ingredientes = Ingredientes.objects.all()
        serializer = IngredientesSerializer(ingredientes, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = IngredientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "DEU CERTO!!"}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Criando as views de Produtos_Ingredientes
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def listar_atualizar_deletar_produto_ingrediente(request, id):
    try:
        produtos_ingredientes = Produtos_Ingredientes.objects.get(pk=id)
    except Produtos_Ingredientes.DoesNotExist:
        return Response({"Mensagem": "Ingredientes do Produto não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = Produtos_IngredientesSerializer(produtos_ingredientes)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = Produtos_IngredientesSerializer(produtos_ingredientes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Ingrediente do Produto atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = Produtos_IngredientesSerializer(produtos_ingredientes, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Ingredientes do Produto atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        produtos_ingredientes.delete()
        return Response({"Mensagem": "Ingredientes do Produto deletado com sucesso"})
    
@api_view(['GET', 'POST'])
def criar_pegar_produto_ingrediente(request):
    if request.method == 'GET':
        produtos_ingredientes = Produtos_Ingredientes.objects.all()
        serializer = Produtos_IngredientesSerializer(produtos_ingredientes, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = Produtos_IngredientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "DEU CERTO!!"}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#Criando as views de Fornecedores
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def listar_atualizar_deletar_fornecedor(request, id):
    try:
        fornecedor = Fornecedores.objects.get(pk=id)
    except Fornecedores.DoesNotExist:
        return Response({"Mensagem": "Fornecedor não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FornecedoresSerializer(fornecedor)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = FornecedoresSerializer(fornecedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Fornecedor atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = FornecedoresSerializer(fornecedor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Fornecedor atualizado com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        fornecedor.delete()
        return Response({"Mensagem": "Fornecedor deletado com sucesso"})
    
@api_view(['GET', 'POST'])
def criar_pegar_fornecedor(request):
    if request.method == 'GET':
        fornecedor = Fornecedores.objects.all()
        serializer = FornecedoresSerializer(fornecedor, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = FornecedoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "DEU CERTO!!"}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Criando as views de Compras
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def listar_atualizar_deletar_compra(request, id):
    try:
        compra = Compras.objects.get(pk=id)
    except Compras.DoesNotExist:
        return Response({"Mensagem": "Compra não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ComprasSerializer(compra)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ComprasSerializer(compra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Compra atualizada com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = ComprasSerializer(compra, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Compra atualizada com sucesso"})
        return Response({"Mensagem": "Formato inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        compra.delete()
        return Response({"Mensagem": "Compra deletada com sucesso"})
    
@api_view(['GET', 'POST'])
def criar_pegar_compra(request):
    if request.method == 'GET':
        compra = Compras.objects.all()
        serializer = ComprasSerializer(compra, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ComprasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "DEU CERTO!!"}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)