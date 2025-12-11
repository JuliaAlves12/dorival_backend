from django.db import models

# Create your models here.

# Criando classe de Cliente, usando uma lista
class Clientes(models.Model):
    TIPO_CLIENTES = [
        ('Regular', 'Regular'),
        ('Premium', 'Premium'),
        ('Vip', 'Vip')
    ]
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=25)
    tipo_cliente = models.CharField(max_length=8, choices=TIPO_CLIENTES)

    def __str__(self):
        return f"Nome: {self.nome} | Email: {self.email} | Tipo: {self.tipo_cliente}"


# Criando classe de Mesas, usando lista
class Mesas(models.Model):
    TIPO_MESAS = [
        ('Livre', 'Livre'),
        ('Ocupada', 'Ocupada'),
        ('Reservada', 'Reservada')
    ]
    numero = models.IntegerField()
    capacidade = models.IntegerField()
    status = models.CharField(max_length=10, choices=TIPO_MESAS)

    def __str__(self):
        return f"Numero: {self.numero} | Capacidade: {self.capacidade} | Status: {self.status}"


# Criando classe de Funcionários
class Funcionarios(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return f"Nome: {self.nome} | Cargo: {self.cargo} | Email: {self.email}"
    

# Criando classe de Pedidos, utilizando lista
class Pedidos(models.Model):
    TIPO_PEDIDO = [
        ('Em Preparação', 'Em Preparação'),
        ('Pronto', 'Pronto'),
        ('Entregue', 'Entregue'),
        ('Cancelado', 'Cancelado')
    ]
    cliente_id = models.ForeignKey(Clientes, on_delete=models.SET_NULL, null=True, blank=True)
    funcionario_id = models.ForeignKey(Funcionarios, on_delete=models.SET_NULL, null=True, blank=True)
    mesa_id = models.ForeignKey(Mesas, on_delete=models.SET_NULL, null=True, blank=True)
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=14, choices=TIPO_PEDIDO)
    observacoes = models.TextField()

    def __str__(self):
        return f"Cliente = {self.cliente_id} | Mesa = {self.mesa_id} | Data e Hora: {self.data_hora} | Status: {self.status} | Observações: {self.observacoes}"
    

# Criando classe de Pagamento, utilizando lista
class Pagamentos(models.Model):
    TIPO_PAGAMENTO = [
       ('Dinheiro', 'Dinheiro'),
       ('Cartão', 'Cartão'),
       ('Pix', 'Pix'),
       ('Boleto', 'Boleto') 
    ]
    pedido_id = models.ForeignKey(Pedidos, on_delete=models.SET_NULL, null=True, blank=True)
    tipo_pagamento = models.CharField(max_length=8, choices=TIPO_PAGAMENTO)
    valor = models.DecimalField(decimal_places=2, max_digits=11)
    data_hora = models.DateTimeField()

    def __str__(self):
        return f"Pedido: {self.pedido_id} | Tipo de Pagamento: {self.tipo_pagamento} | Valor: R${self.valor}"
    

# Criando classe de Categorias
class Categorias(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return f"Nome: {self.nome}"


# Criando classe de Produtos
class Produtos(models.Model):
    categoria_id = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True, blank=True)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    estoque = models.IntegerField()

    def __str__(self):
        return f"Nome: {self.nome} | Preço: R${self.preco} | Estoque: {self.estoque}"
    

# Criando classe de ItensPedido
class ItensPedido(models.Model):
    pedido_id = models.ForeignKey(Pedidos, on_delete=models.SET_NULL, null=True, blank=True)
    produto_id = models.ForeignKey(Produtos, on_delete=models.SET_NULL, null=True, blank=True)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"Pedido: {self.pedido_id} | Produto: {self.produto_id} | Quantidade: {self.quantidade} | Preço Unitário: R${self.preco_unitario}"
    

# Criando classe de Ingredientes
class Ingredientes(models.Model):
    nome = models.CharField(max_length=100)
    quantidade_estoque = models.DecimalField(decimal_places=2, max_digits=10)
    unidade_medida = models.CharField(max_length=20)

    def __str__(self):
        return f"Nome: {self.nome} | Estoque: {self.quantidade_estoque} | Medida: {self.unidade_medida}"
    

# Criando classe de Produtos_Ingredientes
class Produtos_Ingredientes(models.Model):
    produto_id = models.ForeignKey(Produtos, on_delete=models.SET_NULL, null=True, blank=True)
    ingrediente_id = models.ForeignKey(Ingredientes, on_delete=models.SET_NULL, null=True, blank=True)
    quantidade_usada = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"Produto: {self.produto_id} | Ingrediente: {self.ingrediente_id} | Quantidade Usada: {self.quantidade_usada}"
    

# Criando classe de Fornecedores
class Fornecedores(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"Nome: {self.nome} | Contato: {self.contato} | Telefone: {self.telefone} | Email: {self.email}"
    

# Criando classe de Compras
class Compras(models.Model):
    fornecedor_id = models.ForeignKey(Fornecedores, on_delete=models.SET_NULL, null=True, blank=True)
    ingrediente_id = models.ForeignKey(Ingredientes, on_delete=models.SET_NULL, null=True, blank=True)
    quantidade = models.DecimalField(decimal_places=2, max_digits=10)
    data_compra = models.DateTimeField()
    valor_total = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"Fornecedor: {self.fornecedor_id} | Ingrediente: {self.ingrediente_id} | Quantidade: {self.quantidade} | Data da Compra: {self.data_compra} | Valor: R${self.valor_total}"
    
