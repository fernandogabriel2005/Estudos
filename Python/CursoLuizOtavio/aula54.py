import os
lista = []
while True:
    option = input(' Selecione uma opção: \n (1) Inserir item \n (2) Remover item \n (3) Listar \n (4) Sair \n')


    inserir = option.startswith('1')
    if inserir is True:
        item_adicionado = input('Digite a palavra que deseja adicionar à lista: ')
        lista.append(item_adicionado)
        os.system('cls')
        

    remover = option.startswith('2')
    if remover is True:
        for indice, valor in enumerate(lista):
            print(f'{indice}, {valor}')
        item_removido = input('Digite qual deseja apagar: ')
        lista.remove(item_removido)
        print(f'Nova lista: {lista}')
    os.system('cls')

    listar = option.startswith('3')
    if listar is True:
        for indice, valor in enumerate(lista):
            os.system('cls')
            print(indice, valor)
    


    sair = option.startswith('4')
    if sair is True:
        print('Obrigado por usar o programa!')
        os.system('cls')
        break

    


    