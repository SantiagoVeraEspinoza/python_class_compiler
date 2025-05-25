import re
from collections import Counter

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        return ''

def contar_palabras(texto):
    palabras = re.findall(r'\b\w+\b', texto.lower())
    return Counter(palabras)

def mostrar_frecuencias(frecuencias, top_n=10):
    print(f"\nLas {top_n} palabras más comunes son:")
    for palabra, cantidad in frecuencias.most_common(top_n):
        print(f"{palabra}: {cantidad}")

def main():
    nombre_archivo = input("Introduce el nombre del archivo de texto: ")
    texto = leer_archivo(nombre_archivo)
    if texto:
        frecuencias = contar_palabras(texto)
        mostrar_frecuencias(frecuencias)

if __name__ == '__main__':
    main()
