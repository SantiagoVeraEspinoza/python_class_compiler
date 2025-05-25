class ArchivoTemporal:
    def __del__(self):
        print("Archivo temporal eliminado")

a = ArchivoTemporal()
del a