palavra = 'perfume'
letras_acertadas = ''
tentativas = 10

while tentativas > 0:
    letra_digitada = input('Digite UMA letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas UMA letra')
        continue

    if letra_digitada in palavra:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else: 
            palavra_formada += '*'

    if palavra_formada == palavra:
        print('CAMPEÃO!')
        print('Palavra: perfume')
        break



    tentativas -= 1
        