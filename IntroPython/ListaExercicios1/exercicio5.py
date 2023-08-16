numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é ímpar')

print(f'Número par') if numero % 2 == 0 else print('Número impar')
