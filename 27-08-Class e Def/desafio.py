#Desafio

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        print("-------------------------------------")
        print("VEÍCULOS:")
        print(f"Marca do veículo: {self.marca}")
        print(f"Modelo do veículo: {self.modelo}")
        print(f"Ano do veículo: {self.ano}")
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")

carro1 = Carro("Toyota", "Corolla", 2022)
carro2 = Carro("Ford", "Mustang", 2021)
carro3 = Carro("Honda", "Civic", 2023)

carro1.detalhes()
carro2.detalhes()
carro3.detalhes()

class Pessoa:
    def __init__(self, nome, idade, setor):
        self.nome = nome
        self.idade = idade
        self.setor = setor

    def apresentar(self):
        print("------------------------------------------")
        print("FUNCIONÁRIOS: ")
        print(f"O nome do(a) funcionário(a): {self.nome}")
        print(f"Idade do(a) funcionário(a): {self.idade}")
        print(f"Setor do(a) funcionário(a): {self.setor}")
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")


funcionario1 = Pessoa("Júlia Alves", 20, "Engenharia CROSS")
funcionario2 = Pessoa("Dienifer Oliveira", 22, "Staff")
funcionario3 = Pessoa("Beatriz Souza", 19, "Engenharia CROSS")

funcionario1.apresentar()
funcionario2.apresentar()
funcionario3.apresentar()

class Manual:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def informacoes(self):
        print("------------------------------------------")
        print("MANUAL: ")
        print(f"O manual {self.titulo}, escrito por {self.autor}, foi publicado em {self.ano_publicacao}")
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")

livro1 = Manual("Dom Quixote", "Miguel de Cervantes", 1605)
livro2 = Manual(1984, "George Orwell", 1949)
livro3 = Manual("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)


livro1.informacoes()
livro2.informacoes()
livro3.informacoes()

class Produto:
    def __init__(self, nome_produto, preco_produto, quantidade_disponivel):
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto
        self.quantidade_disponivel = quantidade_disponivel

    def mostrar_estoque(self):
        print("------------------------------------------")
        print("PRODUTOS: ")
        print(f"Produto: {self.nome_produto}")
        print(f"Preço: {self.preco_produto}")
        print(f"Estoque: {self.quantidade_disponivel}")
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")

produto1 = Produto("Café", "R$ 14.95", 12)
produto2 = Produto("Protetor Solar", "R$ 59.90", 8)
produto3 = Produto("Hidratante Corporal", "R$ 32.50", 25)

produto1.mostrar_estoque()
produto2.mostrar_estoque()
produto3.mostrar_estoque()

class Treinamento:
    def __init__(self, titulo_treinamento, instrutor_treinamento, duracao_treinamento):
        self.titulo_treinamento = titulo_treinamento
        self.instrutor_treinamento = instrutor_treinamento
        self.duracao_treinamento = duracao_treinamento

    def descricao(self):
        print("------------------------------------------")
        print("TREINAMENTOS: ")
        print(f"Nome do trienamento: {self.titulo_treinamento}")
        print(f"Professor do treinamento: {self.instrutor_treinamento}")
        print(f"Duração de treinamento: {self.duracao_treinamento}")
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")

pessoa1 = Treinamento("Python Básico", "Júlia Reis", "180 Horas")
pessoa2 = Treinamento("Segurança da Informação", "João Roque", "5 Horas")
pessoa3 = Treinamento("Softwares, tudo sobre eles", "Rayane Victoria", "50 Horas")

pessoa1.descricao()
pessoa2.descricao()
pessoa3.descricao()

class Aluno:
    def __init__(self, nome_aluno, curso, nota_final):
        self.nome_aluno = nome_aluno
        self.curso = curso
        self.nota_final = nota_final

    def status(self):
        print("------------------------------------------")
        print("ALUNOS: ")
        print(f"Nome do(a) Aluno(a): {self.nome_aluno}")
        print(f"Curso: {self.curso}")
        print(f"Nota final: {self.nota_final}")
        if self.nota_final > 7:
            print(f"Parábens, você foi: APROVADO(A)!")
            print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
        else:
            print(f"Que pena! Você foi: REPROVADO(A)!")
            print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")

aluno1 = Aluno("Júlia Alves", "SQL Básico", 10)
aluno2 = Aluno("Nicolas Pereira", "Python Básico", 2)
aluno3 = Aluno("Gabriela Santos", "TI - Produtos Internos", 4)

aluno1.status()
aluno2.status()
aluno3.status()