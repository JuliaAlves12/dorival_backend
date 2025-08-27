class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        print(f"A marca de seu veículo é: {self.marca} \nO modelo é: {self.modelo} \nO ano do seu veículo é: {self.ano}.")


carro1 = Carro("Toyota", "Corolla", 2022)
carro2 = Carro("Ford", "Mustang", 2021)
carro3 = Carro("Honda", "Civic", 2023)

carro1.detalhes()
carro2.detalhes()
carro3.detalhes()