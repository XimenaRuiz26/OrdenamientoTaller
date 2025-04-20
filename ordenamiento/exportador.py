import csv
import os

# Mapeo de complejidades teóricas
COMPLEJIDADES = {
    "Bubble Sort": "O(n²)",         
    "Quick Sort": "O(n log n)",      
    "Stooge Sort": "O(n^2.7095)",   
    "Radix Sort": "O(nk)",           
    "Merge Sort": "O(n log n)",     
    "Bitonic Sort": "O(log² n · n)" 
}

def guardar_resultados_csv(resultados, tamaño, archivo="resultados_ordenamiento.csv"):
    crear_archivo = not os.path.exists(archivo)

    with open(archivo, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if crear_archivo:
            writer.writerow(["Tamanio", "Algoritmo", "Tiempo (s)", "Complejidad Teorica"])

        # Ordena resultados de mayor a menor por tiempo
        for algoritmo, tiempo in sorted(resultados.items(), key=lambda x: x[1], reverse=True):
            complejidad = COMPLEJIDADES.get(algoritmo, "N/A")
            writer.writerow([tamaño, algoritmo, f"{tiempo:.8f}", complejidad])
