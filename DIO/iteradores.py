class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.nimeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.contador += 1
        raise StopIteration

for i in MeuIterador():
    print(i)