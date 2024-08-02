import os


lista = []
itens= ''
limpar_terminal = os.system('cls')


while True:
    comeco = input('deseja \n | adiconar [1] | modificar [2] | remover [3] | sair [4] |\n ->: ') 
    
    if comeco == '1':
        limpar_terminal
        iten = input('me informe o item que adiconar na sua lista de compras: ')
        lista.append(iten)
        continue

         
    elif comeco == '2':
        iten = input('informe qual item deseja modificar: ')
                
        if iten in lista:
            indice = lista.index(iten)
        else:
            print('este item nao esta presente na lista, por favor insira um item da lista')
            limpar_terminal
            continue

        item_modificado = input('insira sua modificação: ')
        lista[indice] = item_modificado
            
        print(f'o item {iten} foi modificado por {item_modificado}.')
        print('lista atual \n', lista)
        limpar_terminal
        continue

         
    elif comeco == '3':
        iten =  input('qual item deseja remover: ')
        lista.remove(iten)
        print(f'o item {iten} removido da lista')
        print('lista atual \n', lista)
        limpar_terminal
        continue   
    
    break
# except:
#     print('insira um valor valido')