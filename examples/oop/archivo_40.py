class CuentaRegresiva:
    def __init__(self, inicio):
        self.valor = inicio

    def siguiente(self):
        self.valor -= 1
        return self.valor

c = CuentaRegresiva(5)
print(c.siguiente())