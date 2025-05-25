class Usuario:
    def __init__(self, nombre, edad=None):
        self.nombre = nombre
        self.edad = edad

u = Usuario("Ana")
print(u.nombre, u.edad)