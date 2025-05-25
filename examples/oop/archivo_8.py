class Circulo:
    def __init__(self, radio):
        self._radio = radio

    @property
    def diametro(self):
        return self._radio * 2

c = Circulo(5)
print(c.diametro)