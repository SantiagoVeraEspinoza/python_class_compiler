class SnakeCase:
    def __init__(self, frase):
        self.frase = frase

    def convertir(self):
        return self.frase.lower().replace(" ", "_")

s = SnakeCase("Hola Mundo Python")
print(s.convertir())