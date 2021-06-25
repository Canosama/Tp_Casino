import random
import time

inicio = time.time()
apuestas = 0
for _ in range(0,20):
    fichas = 50
    winrate = 0
    lossrate = 0

    while fichas > 0:
        lista = [0, 1]
        x = random.choices(lista, weights=(0.4, 0.6))
        reset = x.pop(0)
        if reset == 0:
            fichas += 1
            apuestas += 1
            winrate += 1
            print('Ganaste')
        elif reset == 1:
            fichas -= 1
            apuestas += 1
            lossrate += 1
            print('Perdiste')
print(f'Has apostado: {apuestas} veces')
print(f'Has apostado un promedio de: {apuestas/20} veces')
jugadas = winrate + lossrate
print(f'Tu porcentaje de victoria fue de: {((winrate*100) / jugadas):.2f}%:')
fin = time.time()
tiempoTranscurrido = fin - inicio
print(f'Hemos demorado: {tiempoTranscurrido}s')
