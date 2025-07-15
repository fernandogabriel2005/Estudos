# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

nome = 'Fernando'
indice = 0
novo_nome = ' '


while indice < len(nome):
    letra = nome[indice]
    letra += '*'#Índice mais *
    novo_nome += letra
    indice += 1

print(novo_nome)

