from django.urls import path
from .views import listar_atualizar_deletar_cliente, criar_pegar_cliente, listar_atualizar_deletar_mesa, criar_pegar_mesa, listar_atualizar_deletar_funcionarios, criar_pegar_funcionario, listar_atualizar_deletar_pedido, criar_pegar_pedido, listar_atualizar_deletar_pagamento, criar_pegar_pagamento, listar_atualizar_deletar_categoria, criar_pegar_categoria, listar_atualizar_deletar_produto, criar_pegar_produto, listar_atualizar_deletar_itenspedido, criar_pegar_itenspedido, listar_atualizar_deletar_ingrediente, criar_pegar_ingrediente, listar_atualizar_deletar_produto_ingrediente, criar_pegar_produto_ingrediente, listar_atualizar_deletar_fornecedor, criar_pegar_fornecedor, listar_atualizar_deletar_compra, criar_pegar_compra

# Criando as urls de Clientes
urlpatterns = [
    path('clientes/', criar_pegar_cliente, name='listar_criar_cliente'),
    path('clientes/<int:id>/', listar_atualizar_deletar_cliente, name='listar_atualizar_deletar_cliente_especifico'),

# Criando as urls de Funcionários
    path('funcionarios/', criar_pegar_funcionario, name='listar_criar_funcionario'),
    path('funcionarios/<int:id>/', listar_atualizar_deletar_funcionarios, name='listar_atualizar_deletar_funcionario_especifico'),

#  Criando as urls de Produtos
    path('produtos/', criar_pegar_produto, name='listar_criar_produto'),
    path('produtos/<int:id>/', listar_atualizar_deletar_produto, name='listar_atualizar_deletar_produto_especifico'),

# Criando as urls de Categorias
    path('categorias/', criar_pegar_categoria, name='listar_criar_categoria'),
    path('categorias/<int:id>/', listar_atualizar_deletar_categoria, name='listar_atualizar_deletar_categoria_especifica'),

# Criando as urls de Ingredientes
    path('ingredientes/', criar_pegar_ingrediente, name='listar_criar_ingrediente'),
    path('ingredientes/<int:id>/', listar_atualizar_deletar_ingrediente, name='listar_atualizar_deletar_ingrediente_especifico'),

# Criando as urls de Mesas
    path('mesas/', criar_pegar_mesa, name='listar_criar_mesa'),
    path('mesas/<int:id>/', listar_atualizar_deletar_mesa, name='listar_atualizar_deletar_mesa_especifica'),

# Criando as urls de Pedidos
    path('pedidos/', criar_pegar_pedido, name='listar_criar_pedido'),
    path('pedidos/<int:id>/', listar_atualizar_deletar_pedido, name='listar_atualizar_deletar_pedido_especifico'),

# Criando as urls de Itens de Pedido
    path('itenspedido/', criar_pegar_itenspedido, name='listar_criar_itenspedido'),
    path('itenspedido/<int:id>/', listar_atualizar_deletar_itenspedido, name='listar_atualizar_deletar_itens_pedido_especifico'),

# Criando as urls de Pagamentos
    path('pagamentos/', criar_pegar_pagamento, name='listar_criar_pagamentos'),
    path('pagamentos/<int:id>/', listar_atualizar_deletar_pagamento, name='listar_atualizar_deletar_pagamento_especifico'),

# Criando as urls de Fornecedores
    path('fornecedores/', criar_pegar_fornecedor, name='listar_criar_fornecedor'),
    path('fornecedores/<int:id>/', listar_atualizar_deletar_fornecedor, name='listar_atualizar_deletar_fornecedor_especifico'),

# Criando as urls de Compras
    path('compras/', criar_pegar_compra, name='listar_criar_compra'),
    path('compras/<int:id>/', listar_atualizar_deletar_compra, name='listar_atualizar_deletar_compra_especifica'),

# Criando as uls de Produto Ingrediente
    path('produtosingredientes/', criar_pegar_produto_ingrediente, name='listar_criar_ingredientes_produto'),
    path('produtosingredientes/<int:id>/', listar_atualizar_deletar_produto_ingrediente, name='listar_atualizar_deletar_produtos_ingrediente_especifico')
]
