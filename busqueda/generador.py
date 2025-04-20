import random
import os

def generar_archivo(nombre_archivo, cantidad):
    if os.path.exists(nombre_archivo):
        print(f"[✓] El archivo '{nombre_archivo}' ya existe. No se generará de nuevo.")
        return

    # Rango: 8 dígitos => entre 10_000_000 y 99_999_999
    datos = sorted(random.sample(range(10_000_000, 100_000_000), cantidad))
    
    with open(nombre_archivo, 'w') as f:
        f.write('\n'.join(map(str, datos)))

    print(f"[+] Archivo generado: {nombre_archivo}")


