class Lampara:
    def __init__(self):
        self.encendida = False

    def alternar(self):
        self.encendida = not self.encendida

l = Lampara()
l.alternar()
print(l.encendida)