import time

class BusquedaTernaria:
    @staticmethod
    def buscar(arreglo, objetivo):
        def recursiva(arr, izq, der):
            if izq > der:
                return -1
            tercio1 = izq + (der - izq) // 3
            tercio2 = der - (der - izq) // 3

            if arr[tercio1] == objetivo:
                return tercio1
            if arr[tercio2] == objetivo:
                return tercio2

            if objetivo < arr[tercio1]:
                return recursiva(arr, izq, tercio1 - 1)
            elif objetivo > arr[tercio2]:
                return recursiva(arr, tercio2 + 1, der)
            else:
                return recursiva(arr, tercio1 + 1, tercio2 - 1)

        inicio = time.perf_counter()
        indice = recursiva(arreglo, 0, len(arreglo) - 1)
        return indice, time.perf_counter() - inicio
