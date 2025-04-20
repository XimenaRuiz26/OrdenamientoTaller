import time

class BusquedaLineal:
    @staticmethod
    def buscar(arreglo, objetivo):
        inicio = time.perf_counter()
        for i in range(len(arreglo)):
            if arreglo[i] == objetivo:
                return i, time.perf_counter() - inicio
        return -1, time.perf_counter() - inicio
