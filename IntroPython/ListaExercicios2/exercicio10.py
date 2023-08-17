from exercicio4 import gera_numeros_aleatorios

lista = gera_numeros_aleatorios(10)

nomes = ['Roberto', 'Josefa', 'Anastácio', 'Ana', 'Oswaldo']
lista.append(nomes)

lista_inteiros = [numero for numero in lista if isinstance(numero, int)]

print(f'A lista contendo apenas números é \n {lista_inteiros}')
