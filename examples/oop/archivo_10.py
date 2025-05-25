class Motor:
    def arrancar(self):
        print("Motor arrancado")

class Auto:
    def __init__(self):
        self.motor = Motor()

    def encender(self):
        self.motor.arrancar()
        print("Auto encendido")

a = Auto()
a.encender()