class ContadorInstancias:
    total = 0

    def __init__(self):
        ContadorInstancias.total += 1

ContadorInstancias()
ContadorInstancias()
print(ContadorInstancias.total)