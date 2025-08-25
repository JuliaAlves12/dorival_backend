import random

def jogar_advinhação():
    computador = random.randint(1,100)
    tentativas = 10

    print("Bem-Vindo(a) ao nosso Jogo de Advinhação! \nTente advinhar o número secreto.")

    while tentativas > 0:
        escolha = int(input("Digite um número: "))
        if escolha == computador:
            print(f"Parabéns! Você acertou o número escolhido: {computador}")
            print(f"Total de tentativas: {tentativas}")
            break

        elif escolha < computador:
            tentativas -= 1
            print(f"Dica: O número é maior. \nSuas tentativas até agora: {tentativas}.")

        elif escolha > computador:
            tentativas -= 1
            print(f"Dica: O número é menor. \nSuas tentativas até agora: {tentativas}.")

        else:
            print("Digite algo válido!")
    if tentativas == 0:
        print(f"Nossa, que pena. Você não acertou! O número secreto era: {computador}.")


jogar_advinhação()
