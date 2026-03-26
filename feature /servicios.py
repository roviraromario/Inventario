"""
Módulo de servicios del inventario
Contiene funciones CRUD y estadísticas
"""

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un producto al inventario.

    Parámetros:
    inventario (list): lista de productos
    nombre (str): nombre del producto
    precio (float): precio del producto
    cantidad (int): cantidad en stock
    """
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)


def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario.
    """
    if len(inventario) == 0:
        print("Inventario vacío.")
        return

    for producto in inventario:
        print(
            "Producto:", producto["nombre"],
            "| Precio:", producto["precio"],
            "| Cantidad:", producto["cantidad"]
        )


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre.

    Retorna:
    dict o None
    """
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza precio o cantidad de un producto.
    """
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        print("Producto no encontrado.")
        return

    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio

    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad

    print("Producto actualizado.")


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario.
    """
    producto = buscar_producto(inventario, nombre)

    if producto:
        inventario.remove(producto)
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario.

    Retorna:
    dict con métricas
    """

    if len(inventario) == 0:
        return None

    subtotal = lambda p: p["precio"] * p["cantidad"]

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }
