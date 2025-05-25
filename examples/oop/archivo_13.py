class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def resumen(self):
        return f"{self.titulo} escrito por {self.autor}"

libro = Libro("1984", "George Orwell")
print(libro.resumen())