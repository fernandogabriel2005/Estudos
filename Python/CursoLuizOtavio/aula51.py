'''
Introdução ao desempacotamento de tuplas
tuplas são estruturas de dados imutáveis que podem ser usadas para armazenar múltiplos valores.
Desempacotar uma tupla significa atribuir seus valores a variáveis separadas.
'''
#nome1, nome2, nome3 = ['fernando', 'luiz', 'otavio']

_, nome2, *_ = ['fernando', 'luiz', 'otavio']
print(nome2)

