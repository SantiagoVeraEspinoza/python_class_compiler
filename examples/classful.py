import re
from collections import Counter

class AnalizadorDeTexto:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.texto = ''
        self.frecuencias = Counter()

    @classmethod
    def leer_archivo(self):
        try:
            with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
                self.texto = archivo.read()
        except FileNotFoundError:
            print(f"El archivo '{self.nombre_archivo}' no fue encontrado.")

    def contar_palabras(self):
        palabras = re.findall(r'\b\w+\b', self.texto.lower())
        self.frecuencias = Counter(palabras)

    def mostrar_frecuencias(self, top_n=10):
        print(f"\nLas {top_n} palabras más comunes son:")
        for palabra, cantidad in self.frecuencias.most_common(top_n):
            print(f"{palabra}: {cantidad}")

def main():
    nombre_archivo = input("Introduce el nombre del archivo de texto: ")
    analizador = AnalizadorDeTexto(nombre_archivo)
    analizador.leer_archivo()
    if analizador.texto:
        analizador.contar_palabras()
        analizador.mostrar_frecuencias()

if __name__ == '__main__':
    main()
