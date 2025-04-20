import time

class BusquedaBinaria:
    @staticmethod
    def buscar(arreglo, objetivo):
        inicio = time.perf_counter()
        izquierda, derecha = 0, len(arreglo) - 1
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if arreglo[medio] == objetivo:
                return medio, time.perf_counter() - inicio
            elif arreglo[medio] < objetivo:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return -1, time.perf_counter() - inicio
