class GeneradorID:
    actual = 0

    def __init__(self):
        self.id = GeneradorID.actual
        GeneradorID.actual += 1

a = GeneradorID()
b = GeneradorID()
print(a.id, b.id)