class Capitalizador:
    def __init__(self, texto):
        self.texto = texto

    def capitalizar(self):
        return self.texto.title()

c = Capitalizador("hola mundo")
print(c.capitalizar())