a, b = 0, 1
print(f'Inicial {a}')

for _ in range(32):
    if _ != 0:
        a, b = b, a + b
        print(a)
    else:
        print(a)
