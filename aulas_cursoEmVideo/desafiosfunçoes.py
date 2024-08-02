# def numeros (number):
#     for number in range(11):
#         number += 1
#         print (str(number) + number)
# n = numeros(2)   

# #---------------------------------------------

# def contagem(number):
#     for number in range(10):
#         number += 1
#         print (number + 1)  


#---------------------------------------------

# def area (larg, comprimento):
#     print('-' * 30)
#     print('CALCULADORA DE AREA')
#     print('-' * 30)
    
#     return larg * comprimento

# total = area(
#     int(input('me infrome um numero: ')) ,
#     int(input('me informe outro valor: '))
#             )
    
# print(total)

#---------------------------------------------

def escreva (palavras):
    return palavras

result = escreva(
    input('me informe uma palvra: ')
                )
#print(result)

def linha (linhas ):
    numero = len(result)
    
    return (numero + 2) * linhas 

bun = linha('-')

print(bun)
print(result)
print(bun)
