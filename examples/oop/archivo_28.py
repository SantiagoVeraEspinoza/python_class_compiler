class Mensaje:
    def __init__(self, contenido):
        self.contenido = contenido

    def en_mayusculas(self):
        return self.contenido.upper()

m = Mensaje("hola mundo")
print(m.en_mayusculas())