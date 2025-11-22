🌎 **Gestor de Países – Proyecto Integrador Programación I – UTN TUP a Distancia**

Aplicación desarrollada como Trabajo Práctico Integrador (TPI) de la materia Programación I, cuyo objetivo es gestionar información de países mediante un menú interactivo en consola, utilizando listas, diccionarios, funciones, filtros, ordenamientos y estadísticas, con persistencia de datos en CSV.

El propósito del proyecto es aplicar los contenidos aprendidos durante la cursada y afianzar habilidades fundamentales en Python: manejo de estructuras de datos, modularización, validaciones, lectura/escritura de archivos y diseño de un flujo de uso claro para el usuario.
___________________________________________________________________________________________________________________________

🚀 **Instalación y ejecución**
1. Clonar el repositorio
```bash
git clone https://github.com/dannemaximiliano/UTN-TPIntegrador-ProgramacionI.git
cd UTN-TPIntegrador-ProgramacionI
```

2. Verificar versión de Python
Este proyecto requiere Python 3.10 o superior
```bash
python --version
```

3. Ejecutar la aplicación
```bash
python main.py
```
___________________________________________________________________________________________________________________________

📦 **Estructura del proyecto**
```bash
├── datos/
│   └── paises.csv              ← Dataset base utilizado por el sistema
├── main.py                     ← Script principal con el menú y lógica central
└── README.md                   ← Documentación del repositorio
```

📌 Archivos principales
| Archivo              | Descripción                                                                                                       |
| -------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **main.py**          | Contiene el menú y todas las funciones requeridas (agregar, actualizar, buscar, filtrar, ordenar y estadísticas). |
| **datos/paises.csv** | Dataset utilizado para lectura y persistencia.                                                                    |


___________________________________________________________________________________________________________________________
🧭 **Menú principal del programa**

Al ejecutar el sistema, se presenta un menú repetitivo hasta elegir la opción 0 – Fin del programa:

* `1` Agregar país

* `2` Actualizar población y superficie

* `3` Buscar país por nombre

* `4` Filtrar por continente

* `5` Filtrar por rango de población

* `6` Filtrar por rango de superficie

* `7` Ordenar países por nombre

* `8` Ordenar países por población

* `9` Ordenar países por superficie

* `10` Mostrar estadísticas

* `0` Salir

Cada opción invoca una función dedicada y, cuando corresponde, guarda los cambios en el archivo CSV.
___________________________________________________________________________________________________________________________


⚙️ **Funcionalidades principales**

✔ **Validaciones**

* Control de campos vacíos (uso de strip() y repreguntas)

* Control de números positivos (isdigit() + conversión a entero)

* Mensajes de error claros y manejo de entradas inválidas

* Evita fallos por registros incompletos en el CSV

🔍 **Búsquedas y Filtros**

* Búsqueda parcial o exacta por nombre

* Filtrado por continente

* Filtrado por rango de población y superficie

↕ **Ordenamientos**

* Ordenamiento ascendente por: nombre, población y superficie

* Ordenamiento descendente opcional en superficie

📊 **Estadísticas**

* País con mayor y menor población

* Promedio de población y superficie

* Cantidad de países por continente

🧩 **Persistencia de datos**

* Lectura y escritura en CSV

____________________________________________________________________________________________________________________________

👥 **Autores**

María José Garcias   Comision 5

Maximiliano Danne    Comision 14
