class Produto:
    def __init__(self, nome_produto, preco_produto, quantidade_disponivel):
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto
        self.quantidade_disponivel = quantidade_disponivel

    def mostrar_estoque(self):
        print(f"Produto: {self.nome_produto} | Preço: {self.preco_produto} | Quantidade em estoque: {self.quantidade_disponivel}.")

    
cafe = Produto("Café 3 Corações", 14.95, 12)
protetor_solar = Produto("Protetor Solar FPS 50", 59.90, 8)
creme_hidratante = Produto("Creme Hidratante Corporal", 32.50, 25)

cafe.mostrar_estoque()
protetor_solar.mostrar_estoque()
creme_hidratante.mostrar_estoque()