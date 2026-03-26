"""
Módulo de manejo de archivos CSV
"""

import csv


def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.
    """

    if len(inventario) == 0:
        print("Inventario vacío. No se puede guardar.")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:

            writer = csv.writer(archivo)

            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print("Inventario guardado en:", ruta)

    except Exception as e:
        print("Error al guardar:", e)


def cargar_csv(ruta):
    """
    Carga productos desde CSV.

    Retorna:
    lista de productos
    """

    productos = []
    errores = 0

    try:

        with open(ruta, "r", encoding="utf-8") as archivo:

            reader = csv.reader(archivo)

            header = next(reader)

            if header != ["nombre", "precio", "cantidad"]:
                print("Encabezado inválido.")
                return []

            for fila in reader:

                if len(fila) != 3:
                    errores += 1
                    continue

                try:
                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue

                    productos.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except:
                    errores += 1

        print("Productos cargados:", len(productos))
        print("Filas inválidas omitidas:", errores)

        return productos

    except FileNotFoundError:
        print("Archivo no encontrado.")

    except UnicodeDecodeError:
        print("Error de codificación del archivo.")

    return []
