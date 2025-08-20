def raio_circulo(area):
    resultado1 = area / 3.14
    raiz = resultado1 ** (1/2)
    return raiz

area = float(input("Digite a área de seu círculo: "))
resultado2 = raio_circulo(area)
print(resultado2)

raio_circulo(area)