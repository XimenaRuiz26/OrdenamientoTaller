import time
import math

class BusquedaPorSaltos:
    @staticmethod
    def buscar(arreglo, objetivo):
        inicio = time.perf_counter()
        n = len(arreglo)
        paso = int(math.sqrt(n))
        prev = 0

        while prev < n and arreglo[min(paso, n)-1] < objetivo:
            prev = paso
            paso += int(math.sqrt(n))
            if prev >= n:
                return -1, time.perf_counter() - inicio

        for i in range(prev, min(paso, n)):
            if arreglo[i] == objetivo:
                return i, time.perf_counter() - inicio

        return -1, time.perf_counter() - inicio
