import random

palavras = ["maça", "uva", "banana", "melao", "morango", "kiwi", "acerola", "maracuja", "manga", "pitaya"]

print("Bem-Vindo(a) ao Jogo da Forca!")

computador = random.choice(palavras)

letras_corretas = ["_"] * len(palavras)

tentativa = 8

while tentativa > 0:
    print(f"Palavra: {' '.join(letras_corretas)}")
    letra = input("Digite uma letra: ")

    if letra in computador:
        for i in range(len(computador)):
            if computador[i] == letra:
                letras_corretas[i] = letra
    else:
        tentativa -= 1
        print(f"Letra incorreta! Você ainda tem: {tentativa} tentativas.")

    if "_" not in letras_corretas:
        print(f"Parabéns, você ganhou! A palavra correta era: {computador}")
        break

    elif tentativa == 0:
        print(f"Você perdeu! A palavra escolhida era: {computador}")