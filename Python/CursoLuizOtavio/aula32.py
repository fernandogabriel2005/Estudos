print('==================Exercício 1==================')

#Não consegui realizar, copiei o resultado do professor.

numero_digitado = input('Digite um número inteiro: ')

if numero_digitado.isdigit():
     numero_digitado_int = int(numero_digitado)
     par = numero_digitado_int % 2 == 0
     par_impar_texto = 'ímpar'

     if par:
          par_impar_texto = 'par'

     print(f'O número {numero_digitado_int} é {par_impar_texto}')
else:
     print('Você não digitou um número')




print('==================Exercício 2==================')

horario_digitado = input('Digite que horas são: ')
horario_digitado_int = int(horario_digitado)

if horario_digitado_int > 0 and horario_digitado_int <= 11:
    print('Bom dia Usuário!')
if horario_digitado_int >= 12 and horario_digitado_int <= 17:
    print('Boa tarde Usuário!')
if horario_digitado_int > 17:
    print('Boa noite Usuário!')
else:
    print('Por favor, digite um número inteiro')



'''
O professor fez assim:
entrada = input('Digite o horario')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('')
    elif hora >= 18 and hora <= 23:
        print('')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite números inteiros!')
'''

print('==================Exercício 3==================')

nome_digitado = input('Digite seu nome: ')
tamanho_nome = len(nome_digitado)
print(tamanho_nome)

nome_curto = tamanho_nome <= 4
nome_medio = tamanho_nome >= 5 and tamanho_nome <= 6
nome_grande = tamanho_nome > 6

if nome_curto is True:
    print('Seu nome é curto')
if nome_medio is True:
    print('Seu nome é médio')
if nome_grande is True:
    print('Seu nome é grande')


'''
Professor:

nome = input("Digite seu nome")
tamanho_nome = len(nome)

if tamanho_nome > 1:
   if tamanho_nome <= 4:
      print('curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
       print('medio')
    else:
        print('grande')
else:
    print('digite mais de 1 letra')
'''