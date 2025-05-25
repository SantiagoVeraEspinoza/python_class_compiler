class Ordenador:
    def __init__(self, lista):
        self.lista = lista

    def ordenar(self):
        return sorted(self.lista)

o = Ordenador([5, 3, 1, 4])
print(o.ordenar())