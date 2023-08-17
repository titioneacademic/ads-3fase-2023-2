from exercicio4 import gera_numeros_aleatorios

lista = gera_numeros_aleatorios(10)

nomes = ['Roberto', 'Josefa', 'Anastácio', 'Ana', 'Oswaldo']

[lista.append(nome) for nome in nomes]

print(f'Os números da lsita agrupados sem espaço geram a seguinte string:'
      f'\n {"".join([str(item) for item in lista])} ')
