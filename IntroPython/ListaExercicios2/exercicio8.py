from exercicio4 import gera_numeros_aleatorios

numeros = gera_numeros_aleatorios(10)
tamanho_total = 0

for numero in numeros:
    tamanho_total += len(str(numero))
    print(f'{len(str(numero))} caracteres')
print(f'O tamanho total de todos os números juntos é {tamanho_total} caracteres')
