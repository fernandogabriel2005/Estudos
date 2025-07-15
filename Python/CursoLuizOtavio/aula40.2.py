''' Exercício criando uma calculadora '''


while True:

    print('============Bem vindo============')
    numero_um = input('Para iniciarmos, digite o primeiro valor: ')
    numero_dois = input('Agora digite o segundo número: ')
    print('=================================')
    operador = input('Agora, digite o operador que deseja (+-/*): ')


    numero_1_float = 0
    numero_2_float = 0
    confirma = None
    operadores_corretos = '+-/*'
    try:
        numero_1_float = float(numero_um)
        numero_2_float = float(numero_dois)
        confirma = True
    except:
        confirma = None
        
    if confirma is None:
        print('Algum ou os dois valores que digitaste está incorreto.')
        continue

    if len(operador) >= 2:
        print('Digite apenas um operador. ')

    if operador not in operadores_corretos:
        print('Operadores aceitos: +-/* ')
        continue

    if operador == '+':
        print(f'{numero_1_float} {operador} {numero_2_float} = {numero_1_float + numero_2_float}')

    if operador == '-':
        print(f'{numero_1_float} {operador} {numero_2_float} = {numero_1_float - numero_2_float}')

    if operador == '/':
        print(f'{numero_1_float} {operador} {numero_2_float} = {numero_1_float / numero_2_float}')

    if operador == '*':
        print(f'{numero_1_float} {operador} {numero_2_float} = {numero_1_float * numero_2_float}')

    sair = input('Deseja sair? Digite S ou N.').lower().startswith('s')
    
    if sair is True:
        break