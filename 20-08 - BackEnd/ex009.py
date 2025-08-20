def area_retangulo(base, altura):
    area = base * altura
    return area

base = float(input("Diigte a sabe do quadrado: "))
altura = float(input("Digite a altura do quadrado: "))

resultado = area_retangulo(base, altura)
print(resultado)

area_retangulo(base, altura)