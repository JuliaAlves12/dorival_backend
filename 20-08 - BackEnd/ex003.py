import random
def gerar_numeros_aleatorios(n, m):
    if n > m:
        numero_aleatorio = random.randint(m,n)
    else:
        numero_aleatorio = random.randint(n,m)
    return numero_aleatorio

n = int(input("Digite o valor de N: "))
m = int(input("Digite o valor de M: "))

numero = gerar_numeros_aleatorios(n,m)
print(f"Número aleatórios entre {n} e {m} : é {numero}.")