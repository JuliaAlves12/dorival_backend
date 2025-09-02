import random
import pyttsx3
from pyfiglet import figlet_format
import msvcrt
import time

class Bingo:
    def __init__(self):
        # Define as letras e seus intervalos de números
        self.letras_numeros = {
            "B": (1, 15),
            "I": (16, 30),
            "N": (31, 45),
            "G": (46, 60),
            "O": (61, 75)
        }
        # Evitar repetir números já sorteados
        self.sorteados = set()
    
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
        while True:
            letra = self.sortear_letra()
            numero = self.sortear_numero(letra)
            token = f"{letra}{numero}"
            if token not in self.sorteados:
                self.sorteados.add(token)
                return letra, numero  # retorna separadamente

    # Se necessario pode criar outras funções auxiliares

    def jogar(self):
        print(figlet_format("BINGO", font="standard"))
        try:
            while True:
                print("Sorteando em 3...")
                time.sleep(1)
                print("Sorteando em 2...")
                time.sleep(1)
                print("Sorteando em 1...")
                time.sleep(1)
                
                # Sorteia letra e número
                letra, numero = self.sorteio()
                sorteio = f"{letra}{numero}"
                
                # Mostra na tela e fala ao mesmo tempo
                print(f"Número sorteado: {sorteio}")
                self.falar(f"{letra}, {numero}")
                
                # Mensagem para o usuário
                print("\nPressione qualquer tecla para sortear novamente ou Ctrl+C para sair...")
                msvcrt.getch()
        except KeyboardInterrupt:
            print("\nAté a próxima!")

    # Nao mexer nessas abaixo
    def falar(self, texto):
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()


bingo = Bingo()
bingo.jogar()
