import random
import os
from generador import generar_archivo
from graficador import graficar
from exportador import guardar_resultados_csv
from algoritmos.busqueda_lineal import BusquedaLineal
from algoritmos.busqueda_binaria import BusquedaBinaria
from algoritmos.busqueda_ternaria import BusquedaTernaria
from algoritmos.busqueda_saltos import BusquedaPorSaltos

LIMITES = {
    "Lineal": 100_000,
    "Binaria": 1_000_000,
    "Ternaria": 1_000_000,
    "Saltos": 1_000_000
}

def cargar_arreglo_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        return list(map(int, f.read().splitlines()))

def ejecutar_busquedas(arreglo, objetivo, tamaño):
    resultados = {}

    print("\n🔍 Ejecutando búsquedas...")

    if tamaño <= LIMITES["Lineal"]:
        print("⏳ Ejecutando búsqueda lineal...")
        _, t = BusquedaLineal.buscar(arreglo, objetivo)
        print(f"✅ Resultado Lineal: {t:.8f} segundos")
        resultados["Lineal"] = t
    else:
        print("⛔ Búsqueda lineal omitida (tamaño muy grande)")

    print("⏳ Ejecutando búsqueda binaria...")
    _, t = BusquedaBinaria.buscar(arreglo, objetivo)
    print(f"✅ Resultado Binaria: {t:.8f} segundos")
    resultados["Binaria"] = t

    print("⏳ Ejecutando búsqueda ternaria...")
    _, t = BusquedaTernaria.buscar(arreglo, objetivo)
    print(f"✅ Resultado Ternaria: {t:.8f} segundos")
    resultados["Ternaria"] = t

    print("⏳ Ejecutando búsqueda por saltos...")
    _, t = BusquedaPorSaltos.buscar(arreglo, objetivo)
    print(f"✅ Resultado Saltos: {t:.8f} segundos")
    resultados["Saltos"] = t

    return resultados

if __name__ == "__main__":
    for tamaño in [10_000, 100_000, 1_000_000]:
        nombre_archivo = f"datos_{tamaño}.txt"

        print(f"\n📦 Verificando/generando arreglo de tamaño {tamaño}...")
        generar_archivo(nombre_archivo, tamaño)

        arreglo = cargar_arreglo_desde_archivo(nombre_archivo)
        objetivo = arreglo[random.randint(0, tamaño - 1)]
        print(f"🎯 Elemento a buscar: {objetivo}")

        resultados = ejecutar_busquedas(arreglo, objetivo, tamaño)

        print(f"\n📊 Resultados para tamaño {tamaño} (ordenados de mayor a menor):")
        for nombre, tiempo in sorted(resultados.items(), key=lambda x: x[1], reverse=True):
            print(f"🔹 {nombre}: {tiempo:.8f} segundos")

        graficar(resultados, tamaño)
        guardar_resultados_csv(resultados, tamaño)


