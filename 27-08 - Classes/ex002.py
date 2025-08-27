class Pessoa:
    def __init__(self, nome, idade, setor):
        self.nome = nome
        self.idade = idade
        self.setor = setor

    def apresentar(self):
        print(f"Nome do(a) Funcionário(a): {self.nome} \nIdade do(a) Funcionário(a): {self.idade} \nSetor do(a) Funcionário(a): {self.setor}")


funcionario_1 = Pessoa("Júlia Alves", 20, "Engenharia CROSS")
funcionario_2 = Pessoa("Kaique Gabriel", 18, "Infraestrutura - TI")
funcionario_3 = Pessoa("Dienifer Oliveira", 22, "Staff")

funcionario_1.apresentar()
funcionario_2.apresentar()
funcionario_3.apresentar()