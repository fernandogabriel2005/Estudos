#1. Crie três variáveis e atribua os valores a seguir: a=1, b=5.9 e c=‘teste’. A partir disso, retorne o tipo de cada uma das variáveis. 

a = 1
b = 5.9
c = 'teste'

print(type(a))
print(type(b))
print(type(c))

# 2. Troque o valor da variável a por ‘1’ e verifique se o tipo da variável mudou.
a = '1'
print(type(a))


# 3. Faça a soma da variável b com a variável c. Interprete a saída, tanto em caso de execução correta quanto em caso de execução com erro.

b = 5.9
c = 'teste'

try:
    resultado = b  + c
    print(resultado)
except TypeError as e:
    print(e)

# 4. Crie uma lista com números de 0 a 9 (em qualquer ordem). Com ela, faça:
# a. Adicione o número 6
# b. Insira o número 7 na 3ª posição da lista
# c. Remova o elemento 3 da lista
# d. Adicione o número 4
# e. Verifique o número de ocorrências do número 4 na lista

lista = [0,1,2,3,4,5,6,7,8,9]
print(lista)

lista.append(6)
print(lista)

lista.insert(2,7)
print(lista)

lista.remove(3)
print(lista)

lista.append(4)
print(lista)

ocorrencias = lista.count(4)
print (ocorrencias)


# 5. Ainda com a lista criada na questão anterior, faça:
# a. Retorne os primeiros 3 elementos da lista
# b. Retorne os elementos que estão da 3ª posição até a 7ª posição da lista
# c. Retorne os elementos da lista de 3 em 3 elementos
# d. Retorne os 3 últimos elementos da lista
# e. Retorne todos os elementos menos os 4 últimos da lista

primeiros_3 = lista[:3]
print(primeiros_3)

terceiro_ao_setimo = lista[2:7]
print(terceiro_ao_setimo)

de_3_em_3 = lista [::3]
print (de_3_em_3)

ultimos_3 = lista[-3:]
print(ultimos_3)

todos_menos_4ultimos = lista[:-4]
print(todos_menos_4ultimos)

# 6. Com a lista das questões anteriores, retorne o 6º elemento da lista

sexto_elemento = lista[5]
print(sexto_elemento)

# 7. Alterar o valor do 7º elemento da lista para 12

lista[6] = 12
print(lista)

# 8. Inverter a ordem dos elementos na lista

lista.reverse()
print(lista)

# 9. Ordenar a lista

lista.sort()
print(lista)

# 10. Crie uma tupla com números de 0 a 9 (em qualquer ordem) e tente:
# a. Alterar o valor do 3º elemento da tupla para o valor 10
# b. Verificar o índice (posição) do valor 5 na tupla

tupla = (3,7,1,8,0,5,9,2,4,6)
try:
    tupla[2] = 10
except TypeError as e:
    print(e)

indice_5 = tupla.index(5)
print(indice_5)

# Listas são mutáveis - podemos alterar seus elementos (como fizemos no item 7)

# Tuplas são imutáveis - não podemos alterar seus elementos (como vimos no erro do item 10a)

# O método index() funciona tanto para listas quanto para tuplas, retornando a primeira ocorrência do valor

# reverse() inverte a lista in-place, enquanto sort() ordena in-place

# Para ordenar sem modificar a lista original, podemos usar sorted(lista) que retorna uma nova lista ordenada