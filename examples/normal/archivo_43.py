def es_primo(n):
    return n > 1 and all(n % i != 0 for i in range(2, n))

print(es_primo(7))