"""
Closure e funções que retornam outras funções
"""


# def criar_saudacao(saudacao):
#     def saudar(nome):
#         return f'{saudacao}, {nome}!'
#     return saudar


# falar_bom_dia = criar_saudacao('Bom dia')
# falar_boa_noite = criar_saudacao('Boa noite')

# for nome in ['Maria', 'Joana', 'Luiz']:
#     print(falar_bom_dia(nome))
#     print(falar_boa_noite(nome))

#-------------------------------------desafio aula 117--------------------------------

# def mate (duplica):
#     return duplica * 2
# double = mate


# for num in [1, 2, 3, 4, 5]:
#     print (double(num))

# def criar_multiplicador(mutiplicador):
#     def number (numeros):
#         return numeros * mutiplicador
#     return number

# duplicar = criar_multiplicador(2)
# triplicar = criar_multiplicador(3)
# quadriplica = criar_multiplicador(4)

# for num in [1, 2, 3, 4]:
#     print(duplicar(num))
#     print(triplicar(num))
#     print(quadriplica(num))

#------------------------------------------AULA 119-------------------------------------

#AULA SOBRE DICIONARIOS

# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

# pessoa = {
#     'nome': 'celiana',
#     'sobrenome': 'rocha',
#     'idade': 19,
#     'altura': 1.61,
#     'endereço': [
#         {'rua': 'por aí', 'numero': 11111}
#     ]
# }

# print(pessoa['endereço'])
# print()

# for chave in pessoa:
#     print(chave, pessoa[chave])


#----------------------------------AULA 120--------------------------------------------

# Manipulando chaves e valores em dicionários
# pessoa = {}

# ##
# ##

# chave = 'nome'

# pessoa[chave] = 'Luiz Otávio' #pessoa esta recebendo a chave nome na variavel acima
# pessoa['sobrenome'] = 'Miranda' #recebendo cahve sobrenome 


# print(pessoa[chave]) #exibe o dicionario mas apenas o item pedido no caso nome

# pessoa[chave] = 'Maria' #aqui trocou a informação do nome que agr sera `maria`

# del pessoa['sobrenome'] #etsa deletando a cahve sobrenome
# print(pessoa) # uma exibição de como esta atualmeneto após o delete 
# print(pessoa['nome']) #puxando apenas a cahve nome 

# # print(pessoa.get('sobrenome'))
# if pessoa.get('sobrenome') is None: #um if para verificar a existencia de algo, no caso de sobrenome
#     print('NÃO EXISTE')
# else:
#     print(pessoa['sobrenome'])

#acima se casso nao existir ira resultar no print, caso sim no else,
#alias, .get sempre retorna NONE por issso devemos usar o is none como forma de confirmaçao


#--------------------------- AULA 121 ----------------------------------------------------------

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe

# pessoa = {
#     'nome': 'luiz otavio',
#     'sobrenome': 'miranda',
# }
# # print(len(pessoa)) #informa qunatas informações existem no dicionario
# # print(pessoa.keys()) # informa as chaves, parece uma lista mas não
# # print(list(pessoa.values())) #retorn os valores e transforma em lista
# # print(list(pessoa.items())) #retorna as cahves e os valores, no caso aqui como uma lista
# pessoa.setdefault('idade', 0) #adiciona um chave e um valor 
# print(pessoa ['idade'])

#------------------------ AULA 122 -------------------------------------------------------------

# copy - retorna uma cópia rasa (shallow copy)
# import copy

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2],
# }
# d2 = copy.deepcopy(d1)

# d2['c1'] = 1000
# d2['l1'][1] = 999999

# print(d1)
# print(d2)

#para usar um meio que de fato copie tudo de um dicionario ate os subniveis importe copy
#e use copy.deepcopy

#-------------------------------- AULA 123 -----------------------------------------------
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# for x, obj in myfamily.items():
#     print(x)
#     for y in obj:
#         print(y + ':', obj[y])

#--------------------------AULA 124 -------------------------------------------------------

#DESAFIO
# começo = True

# perguntas = [
#     {
#         'pergunta': 'quanto é 2 + 2?',
#         'opcoes' : ['1','3', '4', '5'],
#         'resposta' : '4',
#     },
#     {
#         'pergunta': 'quanto é 5*5?',
#         'opcoes' : ['25','55', '10', '51'],
#         'resposta' : '25',
#     },
#     {
#         'pergunta': 'quanto é 10/2?',
#         'opcoes' : ['4','5', '2', '1'],
#         'resposta' : '5',
#     },
# ]
# qtd_acertos = 0
# for ask in perguntas:
#     print(ask['pergunta'])
#     print('-' * 30)

#     for i, options in enumerate(ask['opcoes']): 
#         print(f'{i})',  options)    
#     print('-' * 30)

#     escolha = input('qual a sua escolha: ')

#     acertou = False
#     escolha_int = None
#     qtd_opcoes = len(options)

#     if escolha.isdigit():
#         escolha_int = int(escolha)

#     if escolha_int is not None:
#         if escolha_int >= 0 and escolha_int < qtd_opcoes:
#             if options[escolha_int] == ask['Resposta']:
#                 acertou = True

#     print()
#     if acertou:
#         qtd_acertos += 1
#         print('Acertou 👍')
#     else:
#         print('Errou ❌')

#     print()


# print('Você acertou', qtd_acertos)
# print('de', len(perguntas), 'perguntas.')

#--------------------------------- AULA 127 -------------------------------------------------

# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# s1 = {1, 2, 3}
# print(3 not in s1)
# for numero in s1:
#     print(numero)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos


# conjunto = {1, 4, 3, 2}
# transform = ...
# print(conjunto)
# print(transform)

#----------------------- AULA 128 ----------------------------------------------------------

#Métodos uteis:
# add, update, clear, discard

# s1 = set()
# s1.add('meu nome é julia') # .add so aceita um valor por vez 
# s1.update(('ola mundo',)) #itera e pode mandar mais valores de uma vez
# s1.update((1,)) # para adicionar um valor sem dar erro poe a virgula
# s1.clear() #limpa meu set 
# s1.discard('ola mundo') #elimina exatamente o valor passado 
# print(s1) 

#------------------------ AULA 129 -------------------------------------

#Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# s3 =  s1 | s2 # une as duas lista em uma, mas nao exibe duplicatas
# s3 = s1 & s2 # exibe apenas os itens presentes nas duas listas 
# s3 = s1 - s2 # apresenta apenas os itens presente no set da equerda
# s3 = s1 ^ s2 # nos retorna a diferença entre os set's 
# print(s3)

# #----------------------- AULA 130 ---------------------------------------

# #exemplo de set 

# letras = set()
# while True:
#     letra = input('Digite: ')
#     letras.add(letra.lower())

#     if 'l' in letras:
#         print('PARABÉNS')
#         break

#     print(letras)

#acima sempre que o0 usuario digitar uma letra ela sera armaxenada dentro do set 

#----------------------- AULA 131 ------------------------------------------

"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def encontrar_primeiro_dupli(lista_de_listas_de_inteiros): #entrando em cada lista e retornando cada numero
    numeros_checados = set() # set vazio para receber os numeros duplicados 
    primeiro_duplicado = -1 # flag 
    
    for numero in lista_de_listas_de_inteiros:
       if numero in numeros_checados:

        numeros_checados.add(numero)

    print()
    print()


for lista in lista_de_listas_de_inteiros:
    encontrar_primeiro_dupli(lista) #esse for esta jogando cada lista dentro do def 

    