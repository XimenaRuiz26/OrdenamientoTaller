import matplotlib.pyplot as plt

def graficar_resultados(resultados, tamaños):
    for i, tamaño in enumerate(tamaños):
        nombres = list(resultados.keys())
        tiempos = [resultados[n][i] if resultados[n][i] is not None else 0 for n in nombres]
        plt.figure(figsize=(10, 5))
        plt.bar(nombres, tiempos, color='skyblue')
        plt.title(f"Tiempos para tamaño {tamaño}")
        plt.ylabel("Tiempo (s)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
