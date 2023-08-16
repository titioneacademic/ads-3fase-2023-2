lista_nomes = ['Emanoela', 'Jonatan', '', 'Kelly', None, 'Henrique', '']

lista_nomes = [nome for nome in lista_nomes if nome and nome.strip()]
print(f'Os itens da lista que não estão em branco ou nulo são: '
      f'\n {lista_nomes}')

