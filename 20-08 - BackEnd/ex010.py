def area_circulo(raio):
    raio = raio ** 2
    pi = raio * 3.14

    return pi

raio = int(input("Digite um número: "))

resultado = area_circulo(raio)
print(resultado)

area_circulo(raio)