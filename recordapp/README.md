# RecordApp - Registro diario de logros y aprendizajes

Aplicación simple en Python para anotar aprendizajes o logros diarios. Guarda los registros en JSON y permite exportar a CSV.

## Tecnologías/librerías
- Interfaz: **Tkinter** (estándar)
- Persistencia: **json**
- Tests: **pytest**

## Estructura
- `main.py` - interfaz y flujo principal
- `logic/data_manager.py` - funciones para leer/escribir JSON y exportar CSV
- `logic/validation.py` - validaciones simples
- `data/registros.json` - archivo de datos de ejemplo
- `tests/test_data.py` - pruebas unitarias con pytest

## Requisitos
- Python 3.8+

Instalar dependencias de test:
```bash
pip install -r requirements.txt

El proyecto RecordApp consiste en la creación de una aplicación funcional desarrollada en Python, que permite registrar y visualizar aprendizajes o logros personales de cada día. Fue diseñado con el objetivo de integrar distintos aspectos del desarrollo de software: interfaz gráfica, persistencia de datos, validación, modularidad y pruebas automatizadas.

## Características principales:

- Interfaz gráfica: se implementó con la librería Tkinter, incluida en la biblioteca estándar de Python. Permite al usuario ingresar la fecha, un estado de ánimo (😊, 😐 o 😔) y una descripción del logro o aprendizaje. Los registros se muestran en una lista con opciones para ver detalles, eliminar y exportar a CSV.

- **Persistencia de datos:** los registros se guardan en un archivo JSON dentro de la carpeta data/. Esto asegura que la información se conserve aunque se cierre la aplicación.

- **Estructura modular:** el proyecto está organizado en distintas carpetas y módulos.
    . main.py contiene la interfaz y la lógica de interacción con el usuario.
    . logic/data_manager.py maneja el guardado, lectura y exportación de los registros.
    . logic/validation.py se encarga de validar las entradas del usuario.
    . tests/test_data.py incluye las pruebas automatizadas.

- **Pruebas unitarias:** se desarrollaron 5 pruebas con Pytest, verificando el correcto funcionamiento del guardado, lectura, eliminación, exportación y validación de datos. Todas las pruebas pasaron exitosamente.

- **Librerías utilizadas:**
    . Tkinter: interfaz gráfica de escritorio.
    . JSON / CSV (módulos estándar): persistencia de datos.
    . Pytest: testing y verificación de calidad.
    . Datetime / OS / Sys: validación y manejo de rutas.

El trabajo se realizó de forma individual.
Se utilizó asistencia de IA como apoyo para la redacción de código y estructura, con posterior validación y pruebas manuales para garantizar el correcto funcionamiento.

## Fundamento didáctico: aprendizajes, desafíos y reflexiones del proceso:

El desarrollo de este proyecto me permitió integrar varios contenidos aprendidos a lo largo del curso, combinando aspectos teóricos y prácticos del lenguaje Python.
Pude aplicar los conceptos de estructuras de control, modularización, manejo de archivos y funciones, además de trabajar con una interfaz gráfica.
Uno de los principales aprendizajes fue entender la importancia de la organización del código. Separar la lógica en distintos módulos (main.py, data_manager.py, validation.py) hizo que el proyecto fuera más claro, fácil de mantener y de probar. También aprendí a usar archivos JSON como una forma simple y efectiva de almacenar datos de manera persistente.
Un aprendizaje valioso fue el uso de pytest para crear pruebas automáticas. Esto me mostró la importancia de comprobar el funcionamiento de cada parte del código, no solo para evitar errores, sino también para asegurar la calidad general del proyecto.
A lo largo del proceso, enfrenté desafíos como errores de importación, rutas de archivos y validaciones incorrectas, que al resolverlos pude reforzar mis habilidades de depuración y pensamiento lógico.
En lo personal, me resultó muy gratificante ver cómo todo funcionaba en conjunto: la interfaz, los datos guardados y las pruebas exitosas. 