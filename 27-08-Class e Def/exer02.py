class Pessoa:
    def __init__(self, nome, idade, setor):
        self.nome = nome
        self.idade = idade
        self.setor = setor

    def apresentar(self):
        print(f"O nome do(a) funcionário(a): {self.nome}")
        print(f"Idade do(a) funcionário(a): {self.idade}")
        print(f"Setor do(a) funcionário(a): {self.setor}")
        print("------------------------------------------")


funcionario1 = Pessoa("Júlia Alves", 20, "Engenharia CROSS")
funcionario2 = Pessoa("Dienifer Oliveira", 22, "Staff")
funcionario3 = Pessoa("Beatriz Souza", 19, "Engenharia CROSS")

funcionario1.apresentar()
funcionario2.apresentar()
funcionario3.apresentar()