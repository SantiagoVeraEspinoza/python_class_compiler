class Contador:
    total = 0

    def __init__(self):
        Contador.total += 1

print(Contador.total)
a = Contador()
b = Contador()
print(Contador.total)