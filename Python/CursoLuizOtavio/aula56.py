'''
split e join com list e str
split -> divide uma str
join -> une uma str
'''

frase = 'Fernando Gabriel Silva, é lindo'
lista_frases = frase.split(',')
lista_palavras = frase.split()
print(lista_palavras)

lista_palavras = frase.split(', ')
print(lista_palavras)


for i, frase in enumerate(lista_palavras):
    lista_frases[i] = lista_palavras[i].strip()