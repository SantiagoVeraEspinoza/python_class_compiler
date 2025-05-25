class Utilidades:
    tasa_iva = 0.21

    @classmethod
    def calcular_iva(cls, monto):
        return monto * cls.tasa_iva

    @staticmethod
    def es_numero_par(n):
        return n % 2 == 0

print(Utilidades.calcular_iva(100))
print(Utilidades.es_numero_par(4))