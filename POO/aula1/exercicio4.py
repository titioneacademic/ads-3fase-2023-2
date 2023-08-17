area_a_pintar = float(input('Insira a quantidade de '
                            'metros a ser pintada: '))

latas_necessarias = area_a_pintar / 54

if latas_necessarias % area_a_pintar != 0:
    latas_necessarias = int(latas_necessarias) + 1

preco_total = latas_necessarias * 80

print(f'A quantidade de latas necessárias é: {latas_necessarias}\n'
      f'Seu custo será R$ {preco_total}.')

