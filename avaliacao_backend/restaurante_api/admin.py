from django.contrib import admin
from .models import Clientes, Mesas, Funcionarios, Pedidos, Pagamentos, Categorias, Produtos, ItensPedido, Ingredientes, Produtos_Ingredientes, Fornecedores, Compras
# Register your models here.

# Registrando os Clientes
admin.site.register(Clientes)

# Registrandp as Mesas
admin.site.register(Mesas)

# Registrando os Funcionarios
admin.site.register(Funcionarios)

# Registrando os Pedidos
admin.site.register(Pedidos)

# Registrando os Pagamentos
admin.site.register(Pagamentos)

# Registrando as Categorias
admin.site.register(Categorias)

# Registrando os Produtos
admin.site.register(Produtos)

# Registrando os ItensPedido
admin.site.register(ItensPedido)

# Registrando os Ingredientes
admin.site.register(Ingredientes)

# Registrando os Produtos_Ingredientes
admin.site.register(Produtos_Ingredientes)

# Registrando os Fornecedores
admin.site.register(Fornecedores)

# Registrando as Compras
admin.site.register(Compras)