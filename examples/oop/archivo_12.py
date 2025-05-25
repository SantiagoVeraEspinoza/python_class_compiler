class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def a_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

t = Temperatura(20)
print(t.a_fahrenheit())