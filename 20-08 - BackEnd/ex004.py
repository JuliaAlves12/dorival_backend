def distancia_pontos(x1,x2,y1,y2):
    x2_menos_x1 = x2 - x1
    y2_menos_y1 = y2 - y1

    x_quadrado = x2_menos_x1 ** 2
    y_quadrado = y2_menos_y1 ** 2

    soma = x_quadrado + y_quadrado

    distancia = soma ** (1/2)

    return distancia

x1 = float(input("Digite um número: "))
x2 = float(input("Digite outro número: "))

y1 = float(input("Digite +1 número: "))
y2 = float(input("Digite o último número: "))

resultado = distancia_pontos(x1,x2,y1,y2)
print(resultado)

distancia_pontos(x1,x2,y1,y2)