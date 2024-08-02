#FUNÇÕES SEM ARGUMENTO

# def meu_decorador(funcao):
#     def envelope():
#         print('faca algo antes de funçao')
#         funcao()
#         print('faca algo apos a função')

#     return envelope

# @meu_decorador
# def ola_mundo():
#     print('ola mundo!')

# ola_mundo()

#FUNÇÕES COM ARGUMENTOS

def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('faca algo antes de funçao')
        funcao(*args, **kwargs) #aqui 
        print('faca algo apos a função')

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f'ola mundo {nome}!')

ola_mundo('joao')
#serve para quando queremos inserir argumentos se numero certo de quantidade

