class Vehiculo:
    def __init__(self, tipo):
        self.tipo = tipo

    @classmethod
    def crear_auto(cls):
        return cls("auto")

v = Vehiculo.crear_auto()
print(v.tipo)