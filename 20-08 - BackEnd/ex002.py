def calcular_imc(peso, altura):
    altura = altura * altura
    imc = peso / altura
    return imc

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

resultado = calcular_imc(peso, altura)
print(f"O seu peso é: {peso}, e sua altura é {altura}. Logo, seu IMC é {resultado}.")