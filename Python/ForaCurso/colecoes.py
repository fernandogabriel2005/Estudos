#Entendendo listas
#Listas são MUTÁVEIS
programadores = ['Fernando', 'Luisana', 'Nancy']
print(programadores)
print('O tipo da variável acima é', type(programadores))
print(f'O números atual de itens na lista é de {len(programadores)}')
print(programadores[2])

#Exemplo alterando uma lista

programadores[1] = 'ALTERACAO'
print(programadores)

programadores.append('Renato')
print(programadores)
programadores.pop(3)
print(programadores)

# lailafernandobaltazar@2005$1969$maturin

#Entendendo tuplas
#Tuplas são IMUTÁVEIS

times = ('corinthians', 'palmeiras', 'santos')
print('Isso é uma tupla por conta dos parênteses', type(times))
print(times[2])

#Entendendo dicionários

dados_cliente = {
    'Nome': 'Fernando',
    'Endereço': 'Sorocaba',
    'Telefone':'919191919'
}
print(dados_cliente)
print(dados_cliente['Nome'])