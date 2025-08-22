# CuentaRegresivaRecursiva2025

**Recursividad** y **Modularización** en Python mediante una cuenta regresiva. 

---

## Objetivos

- Aplicar funciones recursivas en problemas simples.
- Organizar el código en módulos reutilizables.
- Promover buenas prácticas de documentación.
- Fomentar la creatividad.

---

## ¿Cómo pensé la solución?

Para resolver la consigna, decidí dividir el problema en dos partes usando **modularización**:

1. En el archivo `contador.py` puse la **lógica principal**, separando en funciones claras:
   - Una función recursiva que imprime la cuenta regresiva.
   - Una función auxiliar para identificar si un número es par o impar.

2. En el archivo `main.py` coloqué la parte de interacción con el usuario:
   - Solicita un número.
   - Valida que sea positivo.
   - Llama a la función del módulo externo.

---

## Explicación del código

### `contador.py`

- `es_par_o_impar(n)`  
  Esta función determina si el número es par o impar usando el operador módulo (`%`) y devuelve un string como `"4 - par"` o `"3 - impar"`.  
  Es una función auxiliar para **separar responsabilidades** y poder reutilizarla si se extiende el programa.

- `cuenta_regresiva(n)`  
  Es una **función recursiva**. Su funcionamiento es:
  - Si `n < 0`, termina.
  - Imprime si el número actual es par o impar.
  - Si `n == 0`, muestra un mensaje especial de llegada.
  - Si no, se llama a sí misma con `n - 1`.

> Elegí usar recursividad porque se trata de una acción repetitiva que se puede resolver llamando a la misma función hasta alcanzar una condición de corte.

---

### `main.py`

- Usa `input()` para pedir un número entero al usuario.
- Usa `try-except` para validar que sea un número.
- Si es válido y positivo, llama a `cuenta_regresiva()` importada desde el módulo `contador`.

> Separé el código en este archivo para seguir el principio de responsabilidad única: `main.py` se encarga solo de la entrada/salida con el usuario.

---

Al llegar al número 0, el programa muestra un mensaje especial: ¡Llegamos a cero! 
