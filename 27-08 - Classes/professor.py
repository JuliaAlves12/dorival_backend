class SuperHeroi:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

    def salvar(self):
        print(f"Parabéns {self.nome}! Você salvou as pessoas do mundo!")

    def comer(self, comida):
        print(f"{self.nome} comeu {comida}")

    def destruir_carros(self, quantos_carros):
        for i in range(quantos_carros):
            print(f"{self.nome} destruiu um carro com o poder de {self.poder}!")

    def derrotar_vilao(self, nome_vilao):
        print(f"O herói {self.nome} derrotou o grande arqui-inimigo {nome_vilao}.")

super_heroi_1 = SuperHeroi("Spider-Man", "Soltar Teia")
super_heroi_1.salvar()
super_heroi_1.destruir_carros(2)
super_heroi_1.derrotar_vilao("Doende Verde")
super_heroi_1.poder = "dormir"
super_heroi_1.destruir_carros(2)

super_heroi_2 = SuperHeroi("SuperLógica", "Fazer sistemas para condomínios")
super_heroi_2.salvar()
super_heroi_1.salvar()