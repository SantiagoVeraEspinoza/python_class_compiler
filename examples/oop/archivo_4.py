class Gato:
    def sonido(self):
        return "Miau"

class Perro:
    def sonido(self):
        return "Guau"

def hacer_sonido(animal):
    print(animal.sonido())

hacer_sonido(Gato())
hacer_sonido(Perro())