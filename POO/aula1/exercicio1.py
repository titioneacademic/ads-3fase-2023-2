def verifica_par_impar(numero):
    if int(numero) % 2 == 0:
        return 'número par'
    else:
        return 'número ímpar'


while True:
    try:
        entrada = input("Digite um número inteiro: ")
        numero = int(entrada)
        break
    except ValueError:
        print("Entrada inválida, insira um número inteiro.")


print(f'O número {entrada} é um {verifica_par_impar(entrada)}.')
