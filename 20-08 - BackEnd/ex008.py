def area_quadrado(lado):
    area = lado * lado
    return area

lado = float(input("Digite o lado do quadrao: "))

resultado = area_quadrado(lado)
print(resultado)

area_quadrado(lado)