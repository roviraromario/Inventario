from servicios import *
from archivos import *

inventario = []


def es_numero(valor):
    return valor.replace('.', '', 1).isdigit()


while True:

    print("\n================ MENÚ =================")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    opcion = input("Seleccione opción: ")

    if not opcion.isdigit():
        print("Debe ingresar un número.")
        continue

    opcion = int(opcion)

    if opcion == 1:

        nombre = input("Nombre: ")

        precio = input("Precio: ")
        cantidad = input("Cantidad: ")

        if not es_numero(precio) or not cantidad.isdigit():
            print("Datos inválidos.")
            continue

        agregar_producto(
            inventario,
            nombre,
            float(precio),
            int(cantidad)
        )

    elif opcion == 2:
        mostrar_inventario(inventario)

    elif opcion == 3:

        nombre = input("Nombre a buscar: ")

        producto = buscar_producto(inventario, nombre)

        if producto:
            print(producto)
        else:
            print("Producto no encontrado.")

    elif opcion == 4:

        nombre = input("Producto a actualizar: ")

        precio = input("Nuevo precio (enter para omitir): ")
        cantidad = input("Nueva cantidad (enter para omitir): ")

        nuevo_precio = float(precio) if es_numero(precio) else None
        nueva_cantidad = int(cantidad) if cantidad.isdigit() else None

        actualizar_producto(
            inventario,
            nombre,
            nuevo_precio,
            nueva_cantidad
        )

    elif opcion == 5:

        nombre = input("Producto a eliminar: ")
        eliminar_producto(inventario, nombre)

    elif opcion == 6:

        stats = calcular_estadisticas(inventario)

        if stats:
            print("Unidades totales:", stats["unidades_totales"])
            print("Valor total:", stats["valor_total"])
            print("Producto más caro:", stats["producto_mas_caro"]["nombre"])
            print("Mayor stock:", stats["producto_mayor_stock"]["nombre"])
        else:
            print("Inventario vacío.")

    elif opcion == 7:

        ruta = input("Ruta del archivo: ")
        guardar_csv(inventario, ruta)

    elif opcion == 8:

        ruta = input("Ruta del archivo: ")

        productos = cargar_csv(ruta)

        if len(productos) == 0:
            continue

        decision = input("¿Sobrescribir inventario? (S/N): ")

        if decision.lower() == "s":
            inventario = productos
            print("Inventario reemplazado.")

        else:
            for p in productos:

                existente = buscar_producto(inventario, p["nombre"])

                if existente:
                    existente["cantidad"] += p["cantidad"]
                    existente["precio"] = p["precio"]
                else:
                    inventario.append(p)

            print("Inventario fusionado.")

    elif opcion == 9:
        print("Saliendo del sistema.")
        break

    else:
        print("Opción inválida.")
