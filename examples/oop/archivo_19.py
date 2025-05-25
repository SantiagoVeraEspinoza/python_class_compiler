class Semaforo:
    def __init__(self):
        self.color = "rojo"

    def cambiar(self):
        self.color = "verde" if self.color == "rojo" else "rojo"

s = Semaforo()
print(s.color)
s.cambiar()
print(s.color)