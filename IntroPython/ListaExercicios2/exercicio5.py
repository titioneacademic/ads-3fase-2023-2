from exercicio4 import gera_numeros_aleatorios

numeros = gera_numeros_aleatorios(10)
print(f'Lista de números aleatórios: \n {numeros}')

for numero in numeros:
    if numero % 5 == 0:
        print(f'Número múltiplo por 5: {numero}')
        if numero < 95:
            print(f'Número {numero} menor que 95 ')
        elif numero > 1500:
            break
        else:
            continue
