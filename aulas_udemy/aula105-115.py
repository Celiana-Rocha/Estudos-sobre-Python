# def judas(b, c = 10):
#     print(f'estas sao os primeiros numeros {b, c}')
# judas(1, 2)
# judas(1)

#------------------------AULA 107--------------------------------

"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

# 0 é um valor falsy valor não
# def soma(x, y, z=None): #padrão
#     if z is not None:
#         print(f'{x=} {y=} {z=}', x + y + z)
#     else:
#         print(f'{x=} {y=}', x + y)


# soma(1, 2) #parâmetro
# soma(3, 5)
# soma(100, 200)
# soma(7, 9, 0)
# soma(y=9, z=0, x=7)

#----------------------------------- AULA 109---------------------


"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

#x = 1


# def escopo():
#     # global x
#     x = 10

#     def outra_funcao():
#         # global x
#         x = 11
#         y = 2
#         print(x, y)

#     outra_funcao()
#     print(x)


# print(x)
# escopo()
# print(x)

#------------------------------------AULA 113-------------------------

# def numeros (*args):
#     soma = 1
#     for n in args:
#         soma *= n 
#     return soma

# total = numeros (3, 8)
# print(total)

#SEGUNDO CONDIGO

def number (*args):
    multi = 1
    for dig in args:
        multi *= dig
    return multi



result = number(1, 2, 3, 4)
print(result)
if result % 2 == 0:
    print(f'the result is {result} and it is pair')
else:
    print(f'the result is {result} and it is odd')

print(1*2*3*4)

#CODIGO DA AULA___________________________________

# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicação = multiplicar(10, 2, 3, 4, 5)
print(multiplicação)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar' #o else que ficaria aqui é redundonte, não precisaria estar aqui


outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

print(par_impar is outro_par_impar)