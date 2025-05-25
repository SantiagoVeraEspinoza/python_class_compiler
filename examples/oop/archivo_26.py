class Persona:
    def __init__(self, dni):
        self.dni = dni

    def __eq__(self, otro):
        return self.dni == otro.dni

a = Persona("123")
b = Persona("123")
print(a == b)