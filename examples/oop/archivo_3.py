class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def mostrar_saldo(self):
        print(f"Saldo: ${self.__saldo}")

cuenta = CuentaBancaria(1000)
cuenta.mostrar_saldo()