#Operadores condicionais
a = 5
b = 10
if a < b:
    print("a é menor que b")
elif a > b:
    print("a é maior que b")
else:
    print("a é igual a b")

# Operadores condicionais com operadores lógicos
a = 5
b = 10
c = 15
if a < b and b < c:
    print("a é menor que b e b é menor que c")
elif a < b and b > c:
    print("a é menor que b e b é maior que c")

# Operadores condicionais com operadores lógicos e operadores de comparação
a = 5
b = 10
c = 15
if a < b < c:
    print("a é menor que b e b é menor que c")
elif a < b > c:
    print("a é menor que b e b é maior que c")



entrada = input('Você quer "entrar" ou "sair"? ')
if entrada == 'entrar':
    print('Você entrou no sistema.')
elif entrada == 'sair':
    print('Você saiu do sistema.')
else:
    print('Opção inválida. Por favor, digite "entrar" ou "sair".')