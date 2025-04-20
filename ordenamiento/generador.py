import random
import time

def generar_datos(tamaño):
    return [random.randint(10000000, 99999999) for _ in range(tamaño)]

def medir_tiempo(funcion, datos):
    inicio = time.perf_counter()
    funcion(datos.copy())
    fin = time.perf_counter()
    return round(fin - inicio, 4)