#Exercicio 6

lista=[]

numero=int(input("Digite um número: "))
lista.append(numero)
while True:
    if numero >= 1:
        print("Número positivo! Digite um número negativo.")
        numero=int(input("Digite um número: "))
        lista.append(numero)
    elif numero <0:
        print("Número negativo!")
        break
    else:
        print("Digite um número válido.")
        numero=int(input("Digite um número: "))
        lista.append(numero)

maior = max(lista)
print(f"Seu maior número foi: {maior}")

    