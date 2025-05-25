class ListaInvertida:
    def __init__(self, elementos):
        self.elementos = elementos[::-1]

    def __iter__(self):
        return iter(self.elementos)

for item in ListaInvertida([1, 2, 3]):
    print(item)