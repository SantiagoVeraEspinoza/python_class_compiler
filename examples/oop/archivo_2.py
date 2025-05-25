class Animal:
    def hablar(self):
        print("Hace un sonido")

class Perro(Animal):
    def hablar(self):
        print("Guau!")

mi_perro = Perro()
mi_perro.hablar()
# FIN
