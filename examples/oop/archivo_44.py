import random

class Azar:
    def __init__(self):
        self.numero = random.randint(1, 10)

a = Azar()
print(a.numero)