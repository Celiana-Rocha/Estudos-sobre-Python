# import time

# contagem = 10 
# tempo = 1

# for dig in range(contagem , 0, -1 ): 
#     print(dig)
#     time.sleep(tempo)
# print('queima de fogos!!')

#---------------------------------------------------------------

# for dig in range(0, 50, 2):
#     print(dig)

#---------------------------------------------------------------

# n = 3
# numeros = 0
# for dig in range(1, 500, 1):
#     divisao = dig % n
#     if divisao == 0:
#         print(dig) 
#     numeros += dig   
# print(numeros)

#--------------------------------------------------------------

# numero = int(input('me informe de que numero deseja saber a tabuada: '))
# metodo = input('me diga que tipo de calculo deseja fazer - + * /: ')
# tabuada = 0

# for n in range(1, 10+1, ):
#     if metodo == '*':
#         print(f'a tbuada de {numero} é: ', metodo,  n, '=', {numero * n} )
#         tabuada += 1
#     elif metodo == '+':
#         print(f'a tbuada de {numero} é: ', metodo,  n, '=', {numero + n} )
#         tabuada += 1
#     elif metodo == '-':
#         print(f'a tbuada de {numero} é: ', metodo,  n, '=', {numero - n} )
#         tabuada += 1
#     elif metodo == '/':
#         print(f'a tbuada de {numero} é: ', metodo,  n, '=', {numero / n} )
#         tabuada += 1
#     else:
#         print('o valor informado nao e valido')

#--------------------------------------------------------------



# seis_digitos2 = int(input("digite o digito 2: "))
# seis_digitos3 = int(input("digite o digito 3: "))
# seis_digitos4 = int(input("digite o digito 4: "))
# seis_digitos5 = int(input("digite o digito 5: "))
# seis_digitos6 = int(input("digite o digito 6: "))
soma = 0
for dig in range(1, 7):
    seis_digitos1 = int(input("digite o digito 1: "))
    par_ou_nao = dig % 2
    if par_ou_nao == 0:
        soma += par_ou_nao 


    
    print(soma)
