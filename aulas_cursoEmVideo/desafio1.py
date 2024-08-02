#crie um script que leia o nome do usuario e mostre seu nome com uma mensagem de boas vindas 
'''
ome = input('informe seu nome: ') #input para pedir  ainformacao 
msg = 'seja bem vindo(a)' #variavel com a mensagem que sera exibida com o nome do usuario 
print(nome , msg) #funcao print para exibir a pergunta da primeira variavel com a funcao input, logo apos a outra variavel  
'''
'''
dia = input("qual e o dia do seu aniverssario? ")
mes = input("qual o mes que voce nasceu? ")
ano = input("me diga em qual ano voce chegou neste mumdo: ")
v1 = "voce nasceu no dia"
v2 = 'do mes de'
v3 = "no ano de"
print(v1 , dia , v2 , mes , v3 , ano)
'''
''''
dia = input("qual e o dia do seu aniverssario? ")
mes = input("qual o mes que voce nasceu? ")
ano = input("me diga em qual ano voce chegou neste mumdo: ")
print('voce nasceu no dia' , dia , "no mes " , mes , "no ano de " , ano)
'''
'''
n1 = int(input("me informe o primeiro numero: ")) 
n2 = int(input("segundo numero: "))
s = n1 + n2
print( 'o resultado da soma entre {} e {} resulta em: {}' .format(n1, n2, s))

#Variáveis ​​podem armazenar dados de diferentes tipos, e diferentes tipos podem fazer coisas diferentes
'''

#a1 = input("digite qualquer coisa aqui: ")
#print ('o que voce digitou e do tipo: '  , type(a1)  ) 
#print ()

'''
a = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em maiúsculas? {a.isupper()}')
print(f'Está em minúsculas? {a.islower()}')
print(f'Está capitalizado? {a.istitle()}')

'''

#No Python 3.7, não precisa colocar o .format() no final, basta colocar "f" na frente das aspas e inserir os valores dentro dos colchetes, como está acima 

nome = input("qual o seu nome? ")
print(f'prazer em te conhecer {nome :>20}') # o uso do :20 multiplica algo antes dele, pode ser acompanhado de >,<,^.

