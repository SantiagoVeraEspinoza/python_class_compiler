class DiccionarioSeguro:
    def __init__(self):
        self._datos = {}

    def agregar(self, clave, valor):
        self._datos[clave] = valor

    def obtener(self, clave):
        return self._datos.get(clave, None)

d = DiccionarioSeguro()
d.agregar("x", 100)
print(d.obtener("x"))