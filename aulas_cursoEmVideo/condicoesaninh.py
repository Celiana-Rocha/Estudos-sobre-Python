casa = input('me digaqual o valor da casa: ')
salario = input('qual o seu salario: ')
anos = input('em quantos anos deseja pagar: ')
ano = float(anos) * 12 

soma_SALARIO = (float(salario) * 30) / 100
parcelas = float(casa) / ano

if parcelas > soma_SALARIO:
    print('seu emprestimo foi negado')
elif parcelas <= soma_SALARIO:
    print(f'seu emprestimo fou aprovado, sua parcela sera de {parcelas :.2f}')


#---------------------------------------------------------------------------------------------

numero = input('me informe um numero inteiro: ')
opcoes = input('me diga em base decimal deseja \n'
               '[1] binario [2] octal [3] hexadecimal')

if opcoes == '1':
    print('voce escolheu a [1] binario')
    numero 
elif opcoes == '2':
    print('voce escolheu a opcao [2] octal')
else:
    print('a opcão [3] hexadecimal foi escolhida')
