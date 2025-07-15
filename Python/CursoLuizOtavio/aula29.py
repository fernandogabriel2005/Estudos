"""
Introdução ao try/except
try => tentar executar o código
except => ocorreu um erro ao tentar executar
"""
# print(1234)
# print(456)
# int('a')

numero = input('Irei dobrar o número que digitastes')


try:
    print('STR:', numero)
    numero_float = float(numero)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero} é {numero_float * 2:.2f} ')
except:
    print('Isso não é um número')