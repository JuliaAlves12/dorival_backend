class Treinamento:
    def __init__(self, titulo_treinamento, instrutor_treinamento, duracao_treinamento):
        self.titulo_treinamento = titulo_treinamento
        self.instrutor_treinamento = instrutor_treinamento
        self.duracao_treinamento = duracao_treinamento

    def descricao(self):
        print(f"Nome do trienamento: {self.titulo_treinamento}")
        print(f"Professor do treinamento: {self.instrutor_treinamento}")
        print(f"Duração de treinamento: {self.duracao_treinamento}")
        print("------------------------------------------")

pessoa1 = Treinamento("Python Básico", "Júlia Reis", "180 Horas")
pessoa2 = Treinamento("Segurança da Informação", "João Roque", "5 Horas")
pessoa3 = Treinamento("Softwares, tudo sobre eles", "Rayane Victoria", "50 Horas")

pessoa1.descricao()
pessoa2.descricao()
pessoa3.descricao()