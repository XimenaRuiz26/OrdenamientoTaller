from generador import generar_datos, medir_tiempo
from graficador import graficar_resultados

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

def ejecutar_algoritmos(tamaños):
    resultados = {alg: [] for alg in algoritmos}

    for tamaño in tamaños:
        datos = generar_datos(tamaño)
        print(f"\n🔷 Tamaño del arreglo: {tamaño}")
        print("-" * 35)

        for nombre, funcion in algoritmos.items():
            if nombre in limites and tamaño > limites[nombre]:
                print(f"{nombre}: omitido (límite de {limites[nombre]} elementos)")
                resultados[nombre].append(None)
                continue

            print(f"▶ Ejecutando {nombre}...", end=" ")
            tiempo = medir_tiempo(funcion, datos)
            resultados[nombre].append(tiempo)
            print(f"✅ {tiempo} segundos")

        # Mostrar tabla parcial
        print("\n⏱️  Tiempos parciales:")
        print(f"{'Algoritmo':20} {'Tiempo (s)'}")
        for nombre in algoritmos:
            tiempo = resultados[nombre][-1]
            tiempo_str = str(tiempo) if tiempo is not None else "N/A"
            print(f"{nombre:20} {tiempo_str}")

    return resultados

if __name__ == "__main__":
    print("🚀 Comparador de algoritmos de ordenamiento")
    tamaños = [10_000, 100_000, 1_000_000]
    resultados = ejecutar_algoritmos(tamaños)
    graficar_resultados(resultados, tamaños)

    # Tabla final
    print("\n📊 Resumen general:")
    print(f"{'Algoritmo':20}", end='')
    for t in tamaños:
        print(f"{t:>12}", end='')
    print()

    for nombre, tiempos in resultados.items():
        print(f"{nombre:20}", end='')
        for t in tiempos:
            t_str = f"{t:.4f}" if t is not None else "N/A"
            print(f"{t_str:>12}", end='')
        print()
