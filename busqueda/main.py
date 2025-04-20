import random
from generador import generar_arreglo
from graficador import graficar
from algoritmos.busqueda_lineal import BusquedaLineal
from algoritmos.busqueda_binaria import BusquedaBinaria
from algoritmos.busqueda_ternaria import BusquedaTernaria
from algoritmos.busqueda_saltos import BusquedaPorSaltos

# Configura los límites de tamaño para ejecutar ciertos algoritmos
LIMITES = {
    "Lineal": 100_000,   # hasta 100 mil
    "Binaria": 1_000_000,
    "Ternaria": 1_000_000,
    "Saltos": 1_000_000
}

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
        print(f"\n📦 Generando arreglo de tamaño {tamaño}...")
        arreglo = generar_arreglo(tamaño)
        objetivo = arreglo[random.randint(0, tamaño - 1)]
        print(f"🎯 Elemento a buscar: {objetivo}")

        resultados = ejecutar_busquedas(arreglo, objetivo, tamaño)

        print(f"\n📊 Resultados para tamaño {tamaño}:")
        for nombre, tiempo in resultados.items():
            print(f"🔹 {nombre}: {tiempo:.8f} segundos")

        graficar(resultados, tamaño)

