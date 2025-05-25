class Coleccion:
    def __init__(self):
        self.items = []

    def agregar(self, item):
        self.items.append(item)

c = Coleccion()
c.agregar("dato")
print(c.items)