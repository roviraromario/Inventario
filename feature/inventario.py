import csv
inventario = []
def separador():
    print("\n--------------------------------------------------------\n")

def es_numero_valido(valor):
    return valor.replace('.', '', 1).isdigit()

def agregar_producto():
    print("\n--------------------- AGREGAR PRODUCTO ---------------------")
    
    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    precio_texto = input("Precio del producto: ")
    if not es_numero_valido(precio_texto):
        print("------- Debe ingresar un número válido en el precio. -------")
        return
    precio = float(precio_texto)
    
    cantidad_texto = input("Cantidad del producto: ")
    if not cantidad_texto.isdigit():
        print("La cantidad debe ser un número entero.")
        return
    cantidad = int(cantidad_texto)
    
    if precio < 0 or cantidad < 0:
        print("Valores negativos no permitidos.")
        return

    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    separador()
    print("Producto agregado correctamente.")

def mostrar_inventario():
    print("\n------------------- INVENTARIO ------------------------")
    if not inventario:
        print("El inventario está vacío.")
    else:
        for fila in inventario:
            print(f"Nombre: {fila['nombre']}, Precio: {fila['precio']}, Cantidad: {fila['cantidad']}")
    separador()

def buscar():
    print("\n------------------------ BUSCAR ------------------------")
    nombre = input("Nombre del producto a buscar: ").strip()
    encontrado = False
    for buscar_nombre in inventario:
        if buscar_nombre["nombre"].lower() == nombre.lower():
            print(f"Encontrado: {buscar_nombre}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")
    separador()

def actualizar():
    print("\n---------------------- ACTUALIZAR ----------------------")
    nombre = input("Nombre del producto a actualizar: ").strip()
    for buscar_nombre in inventario:
        if buscar_nombre["nombre"].lower() == nombre.lower():
            precio_texto = input(f"Nuevo precio ({buscar_nombre['precio']}): ").strip()
            if precio_texto and not es_numero_valido(precio_texto):
                print("Precio inválido.")
                return
            buscar_nombre['precio'] = float(precio_texto) if precio_texto else p['precio']
            
            cantidad_texto = input(f"Nueva cantidad ({buscar_nombre['cantidad']}): ").strip()
            if cantidad_texto and not cantidad_texto.isdigit():
                print("Cantidad debe ser un entero válido.")
                return
            buscar_nombre['cantidad'] = int(cantidad_texto) if cantidad_texto else buscar_nombre['cantidad']
            
            print("Producto actualizado.")
            separador()
            return
    print("Producto no encontrado.")
    separador()

def eliminar():
    print("\n----------------------- ELIMINAR -----------------------")
    nombre = input("Nombre del producto a eliminar: ").strip()
    for buscar_nombre in inventario:
        if buscar_nombre["nombre"].lower() == nombre.lower():
            inventario.remove(buscar_nombre)
            print("Producto eliminado.")
            separador()
            return
    print("Producto no encontrado.")
    separador()

def calcular_estadisticas():
    print("\n--------------------- ESTADÍSTICAS ---------------------")
    if len(inventario) == 0:
        print("No hay productos.")
    else:
        for i in inventario:
            valor_total += i["precio"]
        print(f"Valor total del inventario: {valor_total}")
        print(f"Cantidad total de productos: {len(inventario)}")
    separador()

def guardar_csv():
    print("\n--------------------- GUARDAR CSV ---------------------")
    with open("inventario.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio", "cantidad"])
        escritor.writeheader()
        escritor.writerows(inventario)
    print("Datos guardados en CSV.")
    separador()

def cargar_csv():
    print("\n--------------------- CARGAR CSV ----------------------")
    try:
        with open("inventario.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            inventario.clear()
            for fila in lector:
                inventario.append({
                    "nombre": fila["nombre"],
                    "precio": float(fila["precio"]),
                    "cantidad": int(fila["cantidad"])
                })
        print("Datos cargados desde CSV.")
    except FileNotFoundError:
        print("No se encontró el archivo CSV.")
    separador()

# Menú principal
estar = "si"
while estar == "si":
    print("\n=========================== MENÚ ===========================")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Calcular estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")
    print("============================================================")

    opcion_texto = input("Seleccione una opción: ").strip()
    if not opcion_texto.isdigit():
        print("Debe ingresar un número.")
        continue

    opcion = int(opcion_texto)

    if opcion == 1:
        agregar_producto()
    elif opcion == 2:
        mostrar_inventario()
    elif opcion == 3:
        buscar()
    elif opcion == 4:
        actualizar()
    elif opcion == 5:
        eliminar()
    elif opcion == 6:
        calcular_estadisticas()
    elif opcion == 7:
        guardar_csv()
    elif opcion == 8:
        cargar_csv()
    elif opcion == 9:
        separador()
        estar = "no"
        print("|Saliendo.......|")
    else:
        print("Opción inválida.")   
