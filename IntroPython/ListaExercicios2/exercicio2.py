palavras = ('Paulo é d4veloper e um b0m músico').split()
palavras_com_numeros = []

for palavra in palavras:
    tem_numero = any(c.isdigit() for c in palavra)
    if tem_numero:
        palavras_com_numeros.append(palavra)

print(f'Palavras com números e letras{palavras_com_numeros}')
