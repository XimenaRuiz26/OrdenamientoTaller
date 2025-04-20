from generador import medir_tiempo
from generador import generar_archivo
from graficador import graficar_resultados
from exportador import guardar_resultados_csv
from algoritmos.bubble_sort import BubbleSort
from algoritmos.quick_sort import QuickSort
from algoritmos.stooge_sort import StoogeSort
from algoritmos.radix_sort import RadixSort
from algoritmos.merge_sort import MergeSort
from algoritmos.bitonic_sort import BitonicSort

# Algoritmos y sus funciones
algoritmos = {
    "Bubble Sort": BubbleSort().ordenar,
    "Quick Sort": QuickSort().ordenar,
    "Stooge Sort": StoogeSort().ordenar,
    "Radix Sort": RadixSort().ordenar,
    "Merge Sort": MergeSort().ordenar,
    "Bitonic Sort": BitonicSort().ordenar
}

# Límites por algoritmo
limites = {
    "Stooge Sort": 1_000,
    "Bubble Sort": 100_000,
    "Bitonic Sort": 100_000
}

def cargar_arreglo_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        return list(map(int, f.read().splitlines()))

def ejecutar_algoritmos(tamaños):
    resultados = {alg: [] for alg in algoritmos}

    for tamaño in tamaños:
        archivo = f"datos_{tamaño}.txt"
        generar_archivo(archivo, tamaño)  # Solo si no existe
        datos = cargar_arreglo_desde_archivo(archivo)

        print(f"\n🔷 Tamaño del arreglo: {tamaño}")
        print("-" * 35)
        tiempos_actuales = {}

        for nombre, funcion in algoritmos.items():
            if nombre in limites and tamaño > limites[nombre]:
                print(f"{nombre}: omitido (límite de {limites[nombre]} elementos)")
                resultados[nombre].append(None)
                continue

            print(f"▶ Ejecutando {nombre}...", end=" ")
            tiempo = medir_tiempo(funcion, datos)
            resultados[nombre].append(tiempo)
            tiempos_actuales[nombre] = tiempo
            print(f"✅ {tiempo} segundos")

        guardar_resultados_csv(tiempos_actuales, tamaño)

        # Mostrar tabla parcial
        print("\n⏱️  Tiempos parciales:")
        print(f"{'Algoritmo':20} {'Tiempo (s)'}")
        for nombre in algoritmos:
            tiempo = resultados[nombre][-1]
            tiempo_str = f"{tiempo:.4f}" if tiempo is not None else "N/A"
            print(f"{nombre:20} {tiempo_str}")

    return resultados

if __name__ == "__main__":
    print("🚀 Comparador de algoritmos de ordenamiento")

    tamaños = [10_000, 100_000, 1_000_000]
    resultados = ejecutar_algoritmos(tamaños)
    graficar_resultados(resultados, tamaños)

    print("\n📊 Resumen general (ordenado de mayor a menor por cada tamaño):")

for idx, tamaño in enumerate(tamaños):
    print(f"\n🔹 Tamaño del arreglo: {tamaño}")
    print(f"{'Algoritmo':20}{'Tiempo (s)':>12}")

    # Lista (algoritmo, tiempo) por tamaño, excluyendo los que no aplican (None)
    tiempos_algoritmos = [
        (nombre, tiempos[idx]) for nombre, tiempos in resultados.items()
        if idx < len(tiempos) and tiempos[idx] is not None
    ]
    # Ordenar de mayor a menor tiempo
    tiempos_ordenados = sorted(tiempos_algoritmos, key=lambda x: x[1], reverse=True)

    for nombre, tiempo in tiempos_ordenados:
        print(f"{nombre:20}{tiempo:.4f}")

    # Para algoritmos que no aplican en ese tamaño
    no_aplica = [
        nombre for nombre, tiempos in resultados.items()
        if idx >= len(tiempos) or tiempos[idx] is None
    ]

    for nombre in no_aplica:
        print(f"{nombre:20}{'N/A':>12}")

