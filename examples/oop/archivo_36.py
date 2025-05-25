class FiltroPar:
    def __init__(self, lista):
        self.lista = lista

    def pares(self):
        return [x for x in self.lista if x % 2 == 0]

f = FiltroPar([1, 2, 3, 4])
print(f.pares())