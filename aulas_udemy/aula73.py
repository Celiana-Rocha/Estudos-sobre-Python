# numeros = range(0, 19, 1)

# for ze in numeros:
#     print(ze)

"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""


palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0 # esta zerado pois a cada novo chute e o laco for outra vez ele somara mais 1

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada #aqui se a letra estiver certa esta variavel ira armazenar ela


# ali em cima so armazeena para chegcar depois
    palavra_formada = '' #esta armazena todas a letras acertadas da palavra da forma que o jogador fez
    for letra_secreta in palavra_secreta: #aqui vamos percorrer letra por letra 
        if letra_secreta in letras_acertadas: 
            palavra_formada += letra_secreta #aqui a letra acertada armazenada vai entrar em palavra_formada
        else:
            palavra_formada += '*' #se o for percorrer a palavra secreta e aletra armazenada estiver certa ela vai ser imprimida e os resto da palavra como ainda e secreta vai ficar ******

# no for se a letra estver certa exibira a letra e se nao ******

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = '' #as variaveis foram traferidas para aca para zerarem tudo e começar outra vez
        numero_tentativas = 0

