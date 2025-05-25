class RelojDigital:
    def __init__(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto

    def mostrar(self):
        return f"{self.hora:02d}:{self.minuto:02d}"

r = RelojDigital(9, 5)
print(r.mostrar())