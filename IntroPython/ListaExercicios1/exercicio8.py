#Escreva um programa que solicite uma lista de números ao
#usuário e exiba o maior e o menor número da lista.
def validar_numero_inteiro(numero):
    while True:
        try:
            return int(numero)
        except ValueError as e:
            print(f'O valor {numero} não é inteiro')
            return False

numeros = input('Insira uma lista de números separados por espaço: ').split()
numeros_inteiros = []

for n in numeros:
    numero_validado = validar_numero_inteiro(n)
    if numero_validado:
        numeros_inteiros.append(numero_validado)

print(f'O maior número da lista é: {max(numeros_inteiros)}'
      f' e o menor número da lista é: {min(numeros_inteiros)}')

