class Acumulador:
    def __init__(self):
        self.total = 0

    def sumar(self, valor):
        self.total += valor

a = Acumulador()
a.sumar(5)
a.sumar(10)
print(a.total)