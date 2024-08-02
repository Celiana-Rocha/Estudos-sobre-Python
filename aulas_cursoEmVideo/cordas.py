#frase = 'ola mundo'
#print('ola' in frase) #ele imprimira True se a palvra estiver na frase.

#frase = 'óla pequeno gafanhoto'
#print(frase.upper()) #deicara a frase inteira em letras maiusculas.

# para faser troca em uma frase fasemps da seguinte forma 

#f = "boa dia"
#f = f.replace('dia', 'noite')
#print(f)

'''
n = str(input('me informe seu nome completo: ')).strip()
print('analisando seu nome...')
print(f'seu nome em maiusculas é:{n.upper()} ')
print('seu nome em minusculas é:{}'.format(n.lower()))
print(f'seu nome te ao todo {len(n) - n.count(' ')} letras')
#usando - n.count('') excluiremos o que estiver entre os parenteses 
 #outra forma de contar as letras do primeiro nome é:
separa = n.split()
print(f'seu primeiro nome é {separa [0]} e possui {len(separa[0])} letras')
#fazendo uma variavel com split e criando uma lista, apenas pedimos a palavra na ordem que esta na lista.
'''
'''
n = int(input('Digite um número entre 0 e 9999: '))
n2 = str(int(10000 + n))
print('O número {} possui, {} milhares.'.format(n, n2[1]))
print('O número {} possui, {} centenas. '.format(n, n2[2]))
print('O número {} possui, {} dezenas. '.format(n, n2[3]))
print('O número {} possui, {} unidades.'.format(n, n2[4]))
'''
#n = str(input('digite algo: '))
#print(f'letra numero tres é:{n[2]}')

# cidade = str(input('em qual cidade vcoe nasceu? ')).strip()
# print(cidade[:5].upper() == 'santos')
#usando == ele se é igual , aqui usamos o .upper para podermos avaliar a opçao de o usuario usa letras maiusculas.