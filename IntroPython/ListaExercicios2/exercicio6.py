from exercicio4 import gera_numeros_aleatorios

numeros = gera_numeros_aleatorios(10)
print(f'A lista de números inicial é {numeros}')

for i in range(1, len(numeros), 2):
    print(f'Numero {numeros[i]} no índice {i}')
