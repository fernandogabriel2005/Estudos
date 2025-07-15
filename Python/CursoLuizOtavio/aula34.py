'''
Repetições
while(enquanto)
executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
'''

condicao = True
'''
    while condicao:
    print(1)
    print(2)
    print(3)
'''
while condicao:
    nome = input('Qual seu nome? ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break