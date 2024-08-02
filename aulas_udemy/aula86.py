# lista = ['lua', 'sol', 'marte', 'venus']
# i = 0 #indica o começo

# for astro in lista:

#     print(i, astro)
#     i += 1

lista = ['Maria', 'Helena', 'Luiz']


indices = range(len(lista)) # 0 1 2 | 0, 3

for indice in indices:
    print(indice, lista[indice]) #a cada vez que ele fizer o laço ele vai imprimir o incie da lista que ele estiver 
                      #ele printa  o nome que o indice estiver, os couxetes pega um item escolhido, ele puxa a informação
                      #no caso aqui queremos o numero que o indice estiver se for 0 pega o nome da lista na posição 0