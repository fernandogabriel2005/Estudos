#tipos de variaveis
# int
idade = 36
# float
altura = 1.80
# str
nome = 'Luiz Otávio'
# bool
ativo = True
# list
numeros = [1, 2, 3, 4, 5]
# dict
pessoa = {
    'nome': 'Luiz Otávio',
    'idade': 36,
    'altura': 1.80,
    'ativo': True
}
# set
numeros_unicos = {1, 2, 3, 4, 5}
# tuple
coordenadas = (10.0, 20.0)
# None
nada = None
# Exibindo os tipos de variáveis
print(type(idade))          # <class 'int'>
print(type(altura))        # <class 'float'>
print(type(nome))          # <class 'str'>
print(type(ativo))         # <class 'bool'>
print(type(numeros))       # <class 'list'>
print(type(pessoa))        # <class 'dict'>
print(type(numeros_unicos)) # <class 'set'>
print(type(coordenadas))   # <class 'tuple'>
print(type(nada))          # <class 'NoneType'>
# Exibindo os valores das variáveis
print(idade)               # 36
print(altura)             # 1.80
print(nome)               # 'Luiz Otávio'
print(ativo)              # True
print(numeros)            # [1, 2, 3, 4, 5]
print(pessoa)             # {'nome': 'Luiz Otávio', 'idade': 36, 'altura': 1.80, 'ativo': True}
print(numeros_unicos)     # {1, 2, 3, 4, 5}
print(coordenadas)        # (10.0, 20.0)
print(nada)               # None

#Diferenças entre listas, tuplas e sets
# Listas são mutáveis, permitem duplicatas e são ordenadas
# Tuplas são imutáveis, permitem duplicatas e são ordenadas
# Sets são mutáveis, não permitem duplicatas e são desordenados
