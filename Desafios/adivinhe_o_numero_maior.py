from random import randint

n = 0
pc1 = 0
pc2 = 0 

while n < 3:
    pc1_escolha = randint(1, 10)
    pc2_escolha = randint(1, 10)

    print(f'A escolha do do PC1 foi {pc1_escolha}')
    print(f'A escolha do PC2 foi {pc2_escolha}')

    if pc1_escolha == pc2_escolha:
        print('tivemos uma empate!!')
        pc1 += 1
        pc2 += 1

    elif pc1_escolha < pc2_escolha:
        print(f'ponto para o PC2!!')
        pc2 += 1

    elif pc1_escolha > pc2_escolha:
        print(f'ponto para o PC1!!')
        pc1 += 1

    n += 1

print('resultado dos jogos!')
print(f'PC1 {pc1}')
print(f'PC2 {pc2}')