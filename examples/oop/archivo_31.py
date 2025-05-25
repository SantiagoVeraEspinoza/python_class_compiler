class Inversor:
    def __init__(self, texto):
        self.texto = texto

    def invertir(self):
        return self.texto[::-1]

i = Inversor("Python")
print(i.invertir())