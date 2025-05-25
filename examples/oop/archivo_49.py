class SumaAcumulada:
    def __init__(self):
        self.total = 0

    def agregar(self, valor):
        self.total += valor

s = SumaAcumulada()
s.agregar(10)
print(s.total)