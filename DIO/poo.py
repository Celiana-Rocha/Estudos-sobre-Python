class Bicicleta:
    
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self): #self e a referencia ao objeto no caso aqui a bicicleta c1
        print('bibiiii')

    def parar(self):
        print('parada')

    def correr(self):
        print('se liga na rapidez mané....')

c1 = Bicicleta('amarelo', 'bmx', 1999, 2000) 
c1.buzinar()
print(c1.cor, c1.modelo, c1.ano, c1.valor)