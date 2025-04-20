import csv
import os

# Mapeo de complejidades teóricas
COMPLEJIDADES = {
    "Lineal": "O(n)",
    "Binaria": "O(log n)",
    "Ternaria": "O(log₃ n)",
    "Saltos": "O(√n)"
}

def guardar_resultados_csv(resultados, tamaño, archivo="resultados_busquedas.csv"):
    crear_archivo = not os.path.exists(archivo)

    with open(archivo, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if crear_archivo:
            writer.writerow(["Tamanio", "Algoritmo", "Tiempo (s)", "Complejidad Teorica"])

        # Ordena resultados de mayor a menor por tiempo
        for algoritmo, tiempo in sorted(resultados.items(), key=lambda x: x[1], reverse=True):
            complejidad = COMPLEJIDADES.get(algoritmo, "N/A")
            writer.writerow([tamaño, algoritmo, f"{tiempo:.8f}", complejidad])
