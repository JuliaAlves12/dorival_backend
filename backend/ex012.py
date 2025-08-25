def binario_para_decimal(binario):
    decimal = 0
    binario = str(binario)[::-1]

    for i in range(len(binario)):
        if binario[i] == '1':
            decimal += 2**i

    return decimal

binario = int(input("Digite um número binário (Somente 0 e 1): "))
print("Decimal:", binario_para_decimal(binario))
