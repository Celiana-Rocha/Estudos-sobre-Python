#print("hello world!")
#comentarios com #
#tudo com # no comeco o compilador ignora 

"""
isso e um comentario
de multiplas linhas, para ter um comentario use trres aspas ou #
"""

#variaveis 

"""
x = 5
y = "john"
print (x)
print (y)
"""

'''
#variaveis nao precisam ser declaradas com tipos
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


x = 5
y = "John"
print(type(x))
print(type(y)) #para ter o tipo de uma variavel use type()
'''

''''
# em py as contas nao precisam estar entre aspas duplas ou simples 
print(1 + 3) adicao
print(3 - 1) subtracao
print(2 / 2) divisao
print(3 * 3) multipliocacao
print (3**2)  / pow (3, 2) potenciação ou exponenciação
'''
# para calcular raiz quadrada e a mesma coisa de fazer a potencia dele por meio 
# 81**(1/2)

#para nao precisar sempre usar .format use f no comeco EX: print(F 'álgo aqui')

'''
com python voce pode usar simbolos matematicos para juntar ou multiplicar palavras 
'oi' + 'ola ' nos da o resultado 'oiola'
'oi'*5 repete oi 5 vezes
'''
#colocando :2f o numero vcoeo indica quantos numeros decimais quer que apareça.
#usando :,2f vcoe pÕe vrigulas em nimeros por exempplo quando indicamos dinheiro.

#MODULOS

#pra fazer um calculo arredondado use 'math.floor' para arrendondar pra baixo, 
#ponha .ceil no lugar de .floor e temos o trunc que elimina tudo da  virgula para frente.

'''
ainda dentro de modulos temos  biblioteca random que gerar um numero aleatorio.
'''
#quando usamos a biblioteca math e utilizamos uma funcao que tenha um x temos que nos atentar se o valor retornado vira da forma que queremos 

#IF ELIF E ELSE

# v1 = input('me infrome um valor: ')
# v2 = input('me informe outro valor: ')
# c = v1 > v2
# if c == True:
#     print (f'o primeiro valor {v1} é maior que o segundo valor {v2}.')

# elif c == True:
#     print(f'o segundo valor {v2} é maior que o primeiro valor {v1}.')


# else: v1 == v2
# print("os dois valores sao iguais")

# n = input('me informe seu nome: ').strip()
# i = input('me infrome sua idade: ') .strip()

# if n:
#     print(f'seu nome é {n}\n Seu nome invertido é {n [::-1]}\n Seu nome contem (ou não) espaços {' ' in n} \n Seu nome contém {len(n) - n.count(' ')} de letras \n A primeira letra do seu nome é: {n [0:1]}')

# else:
#     print('nada foi digitado como resposta.')

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# n = input('me informe um numero inteiro: ')
# i = int(n)
# d = i % 2 == 0 # aqui ja indica o false ou True 

# try: #se tudo o que esruver aqui dentro for falso ou seja nao tiver nada ele dara print no except pq é um erro
#     if d: # se vim igual a 0 ele imprimira o if, pq aqui ele ja sabe se é verdadeiro ou nao no caso ele imrpimira se for True
#         print(f'o numero informado {n} é par.')
#     else: #se nao esse aqui
#         print(f'o nuemro {n} é ímpar.')
# except:
#     print('o que digitado nao é um numero inteiro.')
    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# horas = input('me informe as horas: ')
# h = int(horas)
# try:
#     if h >= 0 and h <= 11:
#         print('good mornning')
#     elif h >= 12 and h <= 17:
#         print('good afternoom')
#     elif h >= 18 and h <= 23:
#         print('good night')
# except:
#     print('nemhum valor informado')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# pname = input('me informe seu primeiro nome: ')
# n = len(pname)
# try:
#     if n >= 1:
#         if n <= 4:
#             print('seu primeiro nome é curto')
#         elif n >= 5 and n <= 6 :
#             print('seu nome é nromal')
#         else:
#             print('seu nome é muito grande')
#     else:
#         print('digita algo sério')
    
# except:
#     print('nada foi informado')

# nome = ['luis', 'davi', 'judas']

# # nome[2]= "lucas"
# lista = nome.copy()
# lista[2] = 'lucas'
# print (lista)
# print (nome)

import math


def add_binary(a, b):
    soma = a + b
    return soma
    
adds = add_binary(3, 2)

binary_number = bin(adds)

print(f'this result {adds} and it is result in binary "{str(binary_number[2:])}"')
