def volume_cilindro(raio, altura):
    raio = raio * raio
    area = (raio * 3.14) * altura
    return area

raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))

resultado = volume_cilindro(raio, altura)
print(resultado)

volume_cilindro(raio, altura)