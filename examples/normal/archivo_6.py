def es_palindromo(palabra):
    return palabra == palabra[::-1]

print(es_palindromo("oso"))