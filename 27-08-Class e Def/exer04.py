class Produto:
    def __init__(self, nome_produto, preco_produto, quantidade_disponivel):
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto
        self.quantidade_disponivel = quantidade_disponivel

    def mostrar_estoque(self):
        print(f"Produto: {self.nome_produto}")
        print(f"Preço: {self.preco_produto}")
        print(f"Estoque: {self.quantidade_disponivel}")
        print("------------------------------------------")

produto1 = Produto("Café", "R$ 14.95", 12)
produto2 = Produto("Protetor Solar", "R$ 59.90", 8)
produto3 = Produto("Hidratante Corporal", "R$ 32.50", 25)

produto1.mostrar_estoque()
produto2.mostrar_estoque()
produto3.mostrar_estoque()