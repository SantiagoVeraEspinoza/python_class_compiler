class Usuario:
    def __init__(self, nombre):
        if not nombre:
            raise ValueError("Nombre no puede estar vacío")
        self.nombre = nombre

u = Usuario("Luis")
print(u.nombre)