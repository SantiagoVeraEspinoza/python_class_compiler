class Multiplicador:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, valor):
        return valor * self.factor

m = Multiplicador(3)
print(m(5))