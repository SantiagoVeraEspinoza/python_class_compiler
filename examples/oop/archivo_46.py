class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

c = Cuadrado(3)
print(c.perimetro())