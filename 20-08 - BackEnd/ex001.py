def decimal_para_binario(num):
    binario = ""
    while num > 0:
        resto = num % 2
        binario = str(resto) + binario
        num = num // 2
    return binario

num = int(input("Digite um número inteiro positivo: "))
print("Número em binário é:", decimal_para_binario(num))