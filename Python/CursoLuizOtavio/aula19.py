"""Operadores de comparação 
Operadores de comparação são usados para comparar valores e retornam um valor booleano (True ou False).
Os principais operadores de comparação são:
- Igualdade (==): Verifica se dois valores são iguais.
- Diferença (!=): Verifica se dois valores são diferentes.
- Maior que (>): Verifica se um valor é maior que o outro.
- Menor que (<): Verifica se um valor é menor que o outro.
- Maior ou igual a (>=): Verifica se um valor é maior ou igual a outro.
- Menor ou igual a (<=): Verifica se um valor é menor ou igual a outro.
"""# Operadores de comparação
nome = 'Fernando'
idade = 19
print(nome == 'Fernando') # True
print(idade != 18) # True
print(idade > 18) # False
print(idade < 18) # False
print(idade >= 19) # True
print(idade <= 19) # True
# Operadores lógicos
# Operadores lógicos são usados para combinar expressões booleanas e retornam um valor booleano (True ou False).
print(nome == 'Fernando' and idade == 19) # True
print(nome == 'Fernando' or idade == 18) # True
print(not (nome == 'Fernando')) # False
