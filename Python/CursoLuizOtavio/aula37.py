contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        continue

    if contador == 40:
        print(contador)
        break

    print(contador)

print('Acabou')