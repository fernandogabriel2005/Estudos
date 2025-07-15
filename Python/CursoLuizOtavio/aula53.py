'''
enumerate() - Enumerate é uma função que permite iterar sobre um objeto iterável e obter o índice de cada elemento.
'''

# Exemplo de uso do enumerate
lista = ('a', 'b', 'c', 'd')
for indice, valor in enumerate(lista):
    print(indice, valor)

lista_enumerada = list(enumerate(lista))
print(lista_enumerada)