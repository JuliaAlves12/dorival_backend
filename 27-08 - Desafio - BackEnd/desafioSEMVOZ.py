import random
import msvcrt
import time

class Bingo:
    def __init__(self):
        self.letras_numeros = {
            "B": (1, 15),
            "I": (16, 30),
            "N": (31, 45),
            "G": (46, 60),
            "O": (61, 75)
        }

    # Sorteia e retorne uma letra entre ('B','I','N','G','O')
    def sortear_letra(self):
        return random.choice(list(self.letras_numeros.keys()))


    # Dado uma letra sortear e retornar um numero possivel
    # ou seja
    # Se for B: Um numero entre  1 e 15
    # Se for I: Um numero entre 16 e 30
    # Se for N: Um numero entre 31 e 45
    # Se for G: Um numero entre 46 e 60
    # Se for O: Um numero entre 61 e 75
    def sortear_numero(self, letra):
        inicio, fim = self.letras_numeros[letra]
        return random.randint(inicio, fim)


    # Utilizando das funçoes de sortear letra e sortear numero
    # Realizar o sorteio da letra e numero e retornar
    # Exemplo B14
    def sorteio(self):
        letra = self.sortear_letra()
        numero = self.sortear_numero(letra)
        return f"{letra}{numero}"

    # Se necessario pode criar outras funções auxiliares
    def jogar(self):
        print("---.---. BINGO ---.---.\n")
        while True:
            print("Sorteando em 3")
            time.sleep(1)
            print("Sorteando em 2")
            time.sleep(1)
            print("Sorteando em 1")
            time.sleep(1)

            sorteio = self.sorteio()
            print(f"Número sorteado: {sorteio}")

            print("\nPressione qualquer tecla para sortear novamente...")
            msvcrt.getch()  # espera tecla para continuar

bingo = Bingo()
bingo.jogar()