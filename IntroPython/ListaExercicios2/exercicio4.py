import random

def gera_numeros_aleatorios(quantidade) -> list:
    numeros_aleatorios = []

    for _ in range(quantidade):
        numeros_aleatorios.append(random.randint(20, 1580))
    return numeros_aleatorios

print(f'A lista de números aleatórios é {gera_numeros_aleatorios(10)}')

