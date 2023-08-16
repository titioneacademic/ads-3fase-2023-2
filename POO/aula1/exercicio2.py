while True:
    try:
        entrada = int(input("Digite um número inteiro: "))
        numero = int(entrada)
        break
    except ValueError:
        print("Entrada inválida, insira um número inteiro.")


print(f'O número {entrada} com duas casas decimais é: {numero:.2f}')
