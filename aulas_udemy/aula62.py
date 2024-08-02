"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321


# nome = 'Maria Helena'  # Iteráveis

# indice = 0 #informa de onde vai começar, que no caso sera da leta M pois esta no 0
# novo_nome = '' #cria uma nova variavel para cada indice
# while indice < len(nome): #len esta determinando ate o indice pode ir, com o tanto de letras definido, teremos o limte da ultima letra
#     letra = nome[indice] #esta variavel pega o nome e logo apos apenas a posicao informada pelo indice
#     novo_nome += f'*{letra}' # printa a letra mais o * a cada volta do laço
#     indice += 1 #soma a cada volta 1 no numero anterior do indice

# novo_nome += '*' #poe ao final do laco um *
# print(novo_nome) 

#                                         AULA 65 EXERCICIO GUIADO

while True:
    numero_1 = input('me informe o primeiro valor: ')
    numero_2 = input('me diga o segundo valor: ')
    operador = input('me diga qual calculo quer fazer (+-/*): ')

    validar_numero = None #para testar se o jegue digitou numeros, tenta por eles para numero  fluatuantes, o none aqui é para testar se algo vai passar ai dentro.
    numerofloat_1 = 0
    numerofloat_1 = 0 #o valor zero serve para a string ser validade, o valor real sera entregue na seguinte acao abaixo.
#definir variaveis dentro de um bloco pode ser muito ruim, pois possa gerar erros futuros.
    try:
        numerofloat_1 = float(numero_1) #entrega de valor as strings validadas.
        numerofloat_2 = float(numero_2)
        validar_numero = True
    except:
        validar_numero = None
    
    if validar_numero is None:
        print('pelo amor de deus cara SÓ NUMEROS!')
        continue #usa  ele para caso isso seja verdade ele sera executado e retornara ao começo do laço.

    if operador not in '+-/*':
        print('MERMAO AS OPCOES TAO LÁ APENAS ELAS.')
        continue

    if len(operador) > 1:
        print('O MANÉ, PELO AMOR DE DEUS VAI CALCULAR OQUE COM DOIS OPERADORES JUNTOS? SÓ UM!')
        continue

    #n1= float(numero_1) / esta acao nao é necessaria pois logo ali em cima criamos variaveis que fazem isso e podem ser utilizadas.
    #n2= float(numero_2)

    if operador == '+':
        print('o resultado é: ', numerofloat_1 + numerofloat_2)
    elif operador == '-':
        print('o resultado é: ', numerofloat_1 - numerofloat_2)
    elif operador =='/':
        print('o resultado é: ', numerofloat_1 / numerofloat_2)
    else:
        print('o resultado é: ', numerofloat_1 * numerofloat_2)
        
        
    sair = input('voce deseja sair? [s]im: ').lower().startswith('s')
#trecho acima torna a resposta em minusculo evitando codugo grade para descobrir se foi um (sim), e depois idetifica se comeca com (s)
    if sair is True: #se a variavel for verdadeira imprima 
        break #para o laco e termina o programa