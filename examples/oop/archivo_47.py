class Doblador:
    def __init__(self, numero):
        self.numero = numero

    def doble(self):
        return self.numero * 2

d = Doblador(6)
print(d.doble())