class Reloj:
    def __init__(self):
        self.segundos = 0

    def tic(self):
        self.segundos += 1
        print(f"{self.segundos} segundo(s)")

r = Reloj()
r.tic()
r.tic()