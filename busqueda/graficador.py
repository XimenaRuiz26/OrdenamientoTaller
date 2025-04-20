import matplotlib.pyplot as plt

def graficar(resultados, tamaño):
    nombres = list(resultados.keys())
    tiempos = list(resultados.values())
    colores = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

    plt.figure(figsize=(10, 6))
    plt.bar(nombres, tiempos, color=colores)
    plt.title(f"Tiempos de búsqueda para {tamaño} elementos")
    plt.ylabel("Tiempo (segundos)")
    plt.xlabel("Algoritmo de búsqueda")
    plt.show()
