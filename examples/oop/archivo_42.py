class Bateria:
    def __init__(self, carga):
        self.carga = carga

    def usar(self, cantidad):
        self.carga = max(0, self.carga - cantidad)

b = Bateria(100)
b.usar(30)
print(b.carga)