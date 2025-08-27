class Treinamento:
    def __init__(self, titulo_treinamento, instrutor_treinamento, duracao_treinamento):
        self.titulo_treinamento = titulo_treinamento
        self.instrutor_treinamento = instrutor_treinamento
        self.duracao_treinamento = duracao_treinamento

    def descricao(self):
        print(f"O seu treinamento é: {self.titulo_treinamento} \nInstrutor do seu curso: {self.instrutor_treinamento} \nCom a duração de: {self.duracao_treinamento} horas")


pessoa1 = Treinamento("Python Básico", "Júlia Reis", 128)
pessoa2 = Treinamento("Segurança da Informação", "João Roque", 5)
pessoa3 = Treinamento("Softwares, quais existem?", "Rayane Victoria", 50)

pessoa1.descricao()
pessoa2.descricao()
pessoa3.descricao()