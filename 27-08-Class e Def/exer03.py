class Manual:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def informacoes(self):
        print(f"O manual {self.titulo}, escrito por {self.autor}, foi publicado em {self.ano_publicacao}")
        print("-------------------------------------------------------------------------")


livro1 = Manual("Dom Quixote", "Miguel de Cervantes", 1605)
livro2 = Manual(1984, "George Orwell", 1949)
livro3 = Manual("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)


livro1.informacoes()
livro2.informacoes()
livro3.informacoes()