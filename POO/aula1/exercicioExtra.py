notas = []

for i in range(4):
    nota = float(input(f'Insira a {i +1}ª nota: '))
    notas.append(nota)

def calcular_media(notas):
    return sum(notas) / len(notas)

media = calcular_media(notas)

if media >= 7:
    print(f'A média do aluno foi {media}!\n'
          f'Aluno aprovado.')
else:
    notas.append(float(input(f'Aluno em recuperação, insira a nota '
                             f'da recuperação: ')))
    nova_media = calcular_media(notas)
    if nova_media >= 5:
        print(f'A média do aluno foi {nova_media}!\n'
              f'Aluno aprovado.')
    else:
        print(f'Aluno foi reprovado com a média {nova_media}!')
