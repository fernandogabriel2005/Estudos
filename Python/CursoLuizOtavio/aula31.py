v1 = 'a'
print(id(v1))

'''
condicao = False

if condicao:
    passou_no_if = True
    print('Passou')
else:
    print('Não')

print(passou_no_if)

código horrível. Declarar variável dentro de if? Mds
'''
# condicao = True
# passou_no_if = None

# if condicao:
#     passou_no_if = True
#     print('Passou')
# else:
#     print('Não')

# print(passou_no_if, passou_no_if is None)
# print(passou_no_if, passou_no_if is not None)

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')

#Legal ver isso no debugador para ver como é lido o código pelo interpretador.