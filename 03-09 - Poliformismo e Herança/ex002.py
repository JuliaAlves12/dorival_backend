class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
       dez_porcento = self.salario * 0.10
       print(f"{self.nome}, Seu bônus é de: R$: {dez_porcento}")

class Gerente(Funcionario):
    def calcular_bonus(self):
        vinte_porcento = self.salario * 0.20
        print(f"{self.nome}, Seu bônus é de: R$: {vinte_porcento}")
    

nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))

tipo = input("Você é funcionário ou gerente? (f/g): ")

if tipo == "f":
    pessoa = Funcionario(nome, salario)
else:
    pessoa = Gerente(nome, salario)


pessoa.calcular_bonus()
