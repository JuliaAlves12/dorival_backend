#Exercício 07
import time

hora = 0
minuto = 0
segundo = 0


while True:
    print(f"{hora}:{minuto}:{segundo}")
    time.sleep(1)

    segundo += 1

    if segundo == 60:
        segundo = 0
        minuto += 1

    elif minuto == 60:
        segundo = 0
        hora += 1

    elif hora == 24:
        segundo = 0
        minuto = 0
        segundo = 0
