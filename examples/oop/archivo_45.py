class Concatenador:
    def __init__(self):
        self.cadena = ""

    def agregar(self, texto):
        self.cadena += texto

c = Concatenador()
c.agregar("Hola")
c.agregar(" Mundo")
print(c.cadena)