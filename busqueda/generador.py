import random
import time

def generar_arreglo(tamaño):
    return sorted([random.randint(10_000_000, 99_999_999) for _ in range(tamaño)])

