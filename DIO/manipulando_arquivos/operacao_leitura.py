arquivo = open('DIO\manipulando_arquivos\lorem.txt', 'r'
               )
#print(arquivo.read()) #entrega astring inteira
#print(arquivo.readline()) #entrega uma linha por vez
#quanto mais print(arquivo.readline()) forem postas ele vai pegando a linha debaixo

#para um uso melhor usar o for com o readlines

# for line in arquivo.readlines():
#     print(line)

#readlines por deabixo dos panos esta iterando uma lista 

while len(linha := arquivo.readline()):
    print(linha)

#dessa forma nos ultilizamos o readline
arquivo.close()