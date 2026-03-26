# Sistema de Gestión de Inventario en Python

## Descripción

Este proyecto es un **sistema de gestión de inventario en consola desarrollado en Python**, que permite administrar productos mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar).

El sistema también permite **guardar y cargar inventarios desde archivos CSV**, además de calcular **estadísticas del inventario**.

Este proyecto está organizado en **módulos**, separando la lógica del programa, los servicios del inventario y el manejo de archivos.

---

# Estructura del Proyecto

El proyecto está dividido en tres archivos principales:

```
inventario/
│
├── main.py
├── servicios.py
├── archivos.py
└── README.md
```

### main.py

Archivo principal que contiene:

* El **menú interactivo del sistema**
* Validación de datos ingresados por el usuario
* Llamadas a las funciones de los módulos `servicios` y `archivos`

### servicios.py

Contiene la **lógica del inventario**, incluyendo:

* Agregar productos
* Mostrar inventario
* Buscar productos
* Actualizar productos
* Eliminar productos
* Calcular estadísticas

### archivos.py

Contiene las funciones para **persistencia de datos en archivos CSV**, incluyendo:

* Guardar inventario
* Cargar inventario
* Validar estructura del archivo

---

# Funcionalidades del Sistema

El sistema cuenta con las siguientes opciones en el menú:

1. Agregar producto
2. Mostrar inventario
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Ver estadísticas del inventario
7. Guardar inventario en CSV
8. Cargar inventario desde CSV
9. Salir del sistema

---

# Estructura de los Productos

Cada producto se guarda como un **diccionario de Python** con la siguiente estructura:

```
{
 "nombre": "Producto",
 "precio": 10.5,
 "cantidad": 20
}
```

El inventario es una **lista de productos**.

---

# Validación de Datos

El sistema valida:

* Que el **precio sea un número**
* Que la **cantidad sea un número entero**
* Que los datos cargados desde CSV sean correctos
* Que no existan valores negativos en precio o cantidad

Si los datos son inválidos, el sistema **evita que el programa falle** y muestra un mensaje de error.

---

# Manejo de Archivos CSV

El sistema permite guardar y cargar inventarios usando archivos CSV.

### Formato del archivo CSV

El archivo debe tener el siguiente encabezado:

```
nombre,precio,cantidad
```

Ejemplo:

```
nombre,precio,cantidad
Laptop,2500,5
Mouse,20,50
Teclado,45,30
```

---

# Estadísticas del Inventario

El sistema calcula automáticamente:

* Total de unidades en inventario
* Valor total del inventario
* Producto más caro
* Producto con mayor cantidad en stock

---

# Manejo de Errores

El programa incluye manejo de errores para evitar fallos comunes como:

* Archivo no encontrado
* Error de codificación
* Filas inválidas en CSV
* Datos no numéricos
* Inventario vacío

Las filas inválidas del CSV se **ignoran automáticamente** y se muestra cuántas fueron omitidas.

---

# Requisitos

Para ejecutar el proyecto se necesita:

* Python 3.x

No se requieren librerías externas, solo la librería estándar:

```
csv
```

---

# Cómo Ejecutar el Programa

1. Colocar los archivos en la misma carpeta:

   * `main.py`
   * `servicios.py`
   * `archivos.py`

2. Ejecutar el archivo principal:

```
python main.py
```

3. Usar el menú para gestionar el inventario.

---

# Posibles Mejoras Futuras

Algunas mejoras que podrían agregarse al sistema:

* Interfaz gráfica con Tkinter
* Exportación a Excel
* Búsqueda por categorías
* Sistema de usuarios
* Base de datos con SQLite
* Control de productos duplicados

---

# Autor

Proyecto desarrollado como práctica de **programación en Python y gestión de inventarios mediante módulos y archivos CSV**.

---
