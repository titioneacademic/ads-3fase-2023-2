lista_pares = [num for num in range(0, 21) if num % 2 ==0]
print(lista_pares)

for num in range(0, 21):
    if num % 2 == 0:
        lista_pares.append(num)
