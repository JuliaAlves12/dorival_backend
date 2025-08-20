def hipotenusa(cateto1, cateto2):
    quadrado1 = cateto1 ** 2
    quadrado2 = cateto2 ** 2

    soma = quadrado1 + quadrado2

    raiz = soma ** (1/2)

    return raiz

cateto1 = float(input("Digite um número: "))
cateto2 = float(input("Digite outro número: "))

resultado = hipotenusa(cateto1, cateto2)
print(resultado)

hipotenusa(cateto1, cateto2)