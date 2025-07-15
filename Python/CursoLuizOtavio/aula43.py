'''
senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_digitada != senha_salva:
    senha_digitada = input(f'Digite a senha {repeticoes}: ')

    repeticoes += 1

print(f'Tentativas: {repeticoes}')

Há esse tipo de loop, mas existe outra forma de fazer isso, que é com for in range, que é mais comum em Python.
'''

# texto = 'Fernando'
# caractere = '*'
# for letra in texto:
#     caractere += letra + '*'
#     print(caractere)

'''
#Exercício 1: Conte quantas vezes a letra 'a' aparece na string "abracadabra".

palavra = 'abracadabra'
i = 0

for letra in palavra:
  if letra == 'a':
    i += 1
    print(f'{letra}  {i}')
  else:
    print(letra)

  

#Exercício 2: Crie uma nova string contendo apenas as consoantes da string "Hello World!".

frase = 'Hello World!'
nova_frase = ''

for letra in frase:
  if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
    nova_frase += letra
print(nova_frase)
'''
'''
Exercício 3: Verifique se a string "racecar" é um palíndromo (lê-se igual de trás para frente) usando um loop.
'''
string = 'racecar'
string_invertida = string[::-1]
nova_frase = ''

while nova_frase != string_invertida:
  for letra in string:
    nova_frase += letra
    print(nova_frase)
print(nova_frase)