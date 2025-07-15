'''
Cuidados com dados mutáveis e imutáveis
- Listas são mutáveis, ou seja, podem ser alteradas após a criação.
- Tuplas são imutáveis, ou seja, não podem ser alteradas após a criação.


lista = ['fernando', 'luiz', 'otavio']

for nome in lista:
    print(nome)
'''


#Exercício: Exiba os índices da lista
lista = ['fernando', 'luiz', 'otavio']
for i in range(len(lista)):
    print(i)
#range é uma função que gera uma sequência de números. Neste caso acima, ela está gerando os índices da lista. 