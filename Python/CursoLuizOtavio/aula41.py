''' while / else '''

string = 'Valor qualquer'

i = 0

while i < len(string):
    letra = string[1]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Nao tem espaço')