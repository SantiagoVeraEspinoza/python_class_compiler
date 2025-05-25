class Producto:
    def __init__(self, precio):
        self.precio = precio

    def __lt__(self, otro):
        return self.precio < otro.precio

a = Producto(50)
b = Producto(30)
print(a < b)