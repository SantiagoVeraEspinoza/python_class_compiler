class Palindromo:
    def __init__(self, texto):
        self.texto = texto

    def es_palindromo(self):
        return self.texto == self.texto[::-1]

p = Palindromo("oso")
print(p.es_palindromo())