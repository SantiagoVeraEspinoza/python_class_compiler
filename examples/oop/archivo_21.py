class Logger:
    def __init__(self, nombre):
        self.nombre = nombre

    def log(self, mensaje):
        print(f"[{self.nombre}] {mensaje}")

l = Logger("Sistema")
l.log("Inicio")