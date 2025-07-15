"""
Fatiamento de strings
Fatiamento é uma técnica que permite acessar partes específicas de uma string.
A sintaxe básica é: string[início:fim:passo]
"""

variavel = 'Olá, mundo!'
print(variavel[0])  # Acessa o primeiro caractere
print(variavel[1])  # Acessa o segundo caractere
print(variavel[0:5])  # Acessa do primeiro ao quinto caractere
print(variavel[0:5:2])  # Acessa do primeiro ao quinto caractere pulando de 2 em 2
print(variavel[0:])  # Acessa do primeiro caractere até o final
print(variavel[:5])  # Acessa do início até o quinto caractere
print(variavel[0:5:1])  # Acessa do primeiro ao quinto caractere com passo 1
print(variavel[0:5:3])  # Acessa do primeiro ao quinto caractere pulando de 3 em 3

#len(variavel)  # Retorna o tamanho da string
print(variavel[0:len(variavel)])  # Acessa o último caractere