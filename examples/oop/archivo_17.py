class Punto3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Punto3D({self.x}, {self.y}, {self.z})"

p = Punto3D(1, 2, 3)
print(p)