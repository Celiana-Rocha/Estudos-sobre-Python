
cpf = '18901525607'
numeros = cpf[:9]
soma = 0
divisao = 10

for i in numeros:
    
    soma += int(i) * divisao
    divisao -= 1

resultado = (soma * 10) % 11

if resultado <= 9:
    print(resultado)
else:
    print(0)

numeros2 = numeros + str(resultado)
soma_segundo_num = 0
divisao2 = 11

for dig in numeros2:
    soma_segundo_num += int(dig) * divisao2
    divisao2 -= 1

resultado2 = (soma_segundo_num * 10) % 11

if resultado2 <= 9:
    print(resultado2)
else:
    print('deu erro')


