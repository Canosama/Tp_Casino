import random
fichas= 50
apuestas = 0


while fichas >= 0 and apuestas < 300:
    lista = [0, 1]
    x = random.choices(lista, weights=(0.4, 0.6))
    reset = x.pop(0)
    if reset == 0:
        fichas += 1
        apuestas += 1
        print('Ganaste')
    elif reset == 1:
        fichas -= 1
        apuestas += 1
        print('Perdiste')




print(f'Has apostado: {apuestas} veces')