def numero_digitos(num):
    return len(str(num))

num = int(input("Digite um número inteiro: "))
print(f"O número {num} possui {numero_digitos(num)} de digitos.")